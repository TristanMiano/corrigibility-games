"""Exact arithmetic and rational root enclosures for funded notes 079--093.

These check formulas, participation margins and a whole prior interval.
They are not a complete-tree audit of the cash/escrow interface in 081.
Run: python experiments/r0004_funded_checks.py
"""
from fractions import Fraction as F
from math import isqrt


def sqrt_bounds(value, digits=40):
    """Certified rational enclosure, using integer arithmetic only."""
    value = F(value)
    assert value >= 0
    scale = 10**digits
    numerator = isqrt(value.numerator*scale*scale//value.denominator)
    lower = F(numerator, scale)
    upper = lower if lower*lower == value else F(numerator+1, scale)
    assert lower*lower <= value <= upper*upper
    return lower, upper


def small_root_bounds(receiver_cost, next_value, ell, digits=40):
    # Stable form of the smaller root of mu^2-A*mu+B=0.
    coefficient = 1-ell+next_value
    constant = receiver_cost+next_value
    lower, upper = sqrt_bounds(coefficient*coefficient-4*constant, digits)
    return (2*constant/(coefficient+upper),
            2*constant/(coefficient+lower))


def continuous_outside(*, p=F(1,2), b=F(1), B=F(1899,10000),
                       x=F(1,10), f=F(1,1000),
                       costs=(F(1,150),)*3, requests=(F(1,30000),)*3,
                       fee_s=F(1,10000), fee_r=F(1,10000), digits=40):
    assert B+fee_s == 2*b*x-x*x
    ell = x*x-B+fee_r
    assert ell < 0
    zlo = zhi = F(0)
    posteriors = []
    for cost in reversed(requests):
        lo = small_root_bounds(cost,zlo,ell,digits)[0]
        hi = small_root_bounds(cost,zhi,ell,digits)[1]
        assert 0 < lo <= hi < F(1,2)
        posteriors.insert(0,(lo,hi))
        # This map and the root are increasing on this low-posterior branch.
        zlo = lo*(1-lo-ell)/(1-lo)
        zhi = hi*(1-hi-ell)/(1-hi)
    qbounds = []
    for i,(lo,hi) in enumerate(posteriors):
        entry = f if i == 0 else costs[i-1]
        gainlo = 2*b*(1-hi)-(1-hi)**2
        gainhi = 2*b*(1-lo)-(1-lo)**2
        qbounds.append((1-entry/gainlo,1-entry/gainhi))
    qlo = qhi = F(1)
    elo = ehi = f
    for (lo,hi),(qmin,qmax),cost in zip(posteriors,qbounds,costs):
        elo += qlo*(1-qmax)*(2*b*lo+lo*lo)
        ehi += qhi*(1-qmin)*(2*b*hi+hi*hi)
        qlo *= qmin
        qhi *= qmax
        elo += qlo*cost
        ehi += qhi*cost
    return dict(ell=ell,posteriors=posteriors,qbounds=qbounds,
                excess=(elo,ehi),receiver_excess=(zlo,zhi),
                sender=(b*b+p*elo,b*b+p*ehi),
                receiver=((1-p)*ell+p*zlo,(1-p)*ell+p*zhi))


def funded_package(*, p=F(1,2), b=F(1), a=F(3,10),
                   B=F(1899,10000), x=F(1,50), f=F(1,1000),
                   costs=(F(1,150),)*3, requests=(F(1,30000),)*3,
                   fee_s=F(1,10000), fee_r=F(1,10000),
                   early_s=F(1,1000), early_r=F(1,1000), update_r=F(1,100)):
    delta = 2*(b-a)*x-x*x-fee_s
    transfer = B-delta
    ell = x*x-delta+fee_r
    D = (1-a)**2
    gain = (1-a)*(2*b-1-a)
    effective = D-ell
    posteriors = [F(0)]*(len(costs)+1)
    for i in reversed(range(len(costs))):
        posteriors[i] = posteriors[i+1]+(1-posteriors[i+1])*requests[i]/effective
    q = [1-f/gain]+[1-cost/gain for cost in costs[:-1]]
    product = F(1)
    expense, false_positive = f, F(0)
    for i in range(len(costs)):
        false_positive += p*product*posteriors[i]*(1-q[i])/(1-posteriors[i])
        product *= q[i]
        expense += product*costs[i]
    excess = p*effective*posteriors[0]/(1-posteriors[0])
    low_receiver = (a+x)**2-delta+fee_r
    sender = (1-p)*(b-a)**2+p*b*b+p*expense+transfer+early_s
    receiver = ((1-p)*low_receiver+excess+2*a*(1-a-x)*false_positive
                -transfer+update_r+early_r)
    return dict(sender=sender,receiver=receiver,expense=expense,
                excess=excess,false_positive=false_positive,
                C_probability=p*product,posteriors=posteriors,q=q,
                low_receiver=low_receiver,ell=ell,delta=delta,transfer=transfer,
                current_receiver=p*a*a+(1-p)*ell+excess)


def ordinary_combat_bound(*, p, b=F(1), a=F(0), B=F(1899,10000),
                          damage_s=F(5), weight=F(2)):
    eta = p*damage_s/(damage_s+2*b-1)
    assert weight >= 1+eta/(1-p)
    denominator = (1-p)*(1+weight)+eta
    numerator = b*(1-p+eta)+weight*a*(1-p)
    assert 0 <= numerator/denominator <= 1
    bound = (b*b+(2*b-1)*eta+weight*a*a-numerator*numerator/denominator
             +(1-weight)*B)
    return bound


def audit_funded_witness():
    package = funded_package()
    outside = continuous_outside()
    assert outside['sender'][0] > package['sender']
    assert outside['receiver'][0] > package['receiver']
    bound = ordinary_combat_bound(p=F(1,2))
    ordinary_sender_lower = bound-2*outside['receiver'][1]
    assert ordinary_sender_lower > package['sender']

    # Certify the whole interval using the monotonicities proved in 081,
    # not by treating a finite sample as a universal parameter check.
    low, high = F(9,20),F(11,20)
    atlow, athigh = funded_package(p=low),funded_package(p=high)
    outlow, outhigh = continuous_outside(p=low),continuous_outside(p=high)
    E0lo,E0hi = outside['excess']
    zlo,zhi = outside['receiver_excess']
    As = F(51,100)
    sender_slope_upper = -As+E0hi-package['expense']
    assert sender_slope_upper < 0
    assert outhigh['sender'][0]-athigh['sender'] > F(66,1000)
    Ar = F(637,2500)
    receiver_slope_lower = (Ar+zlo-2*package['excess']
                           -4*F(3,10)*F(17,25)*package['false_positive'])
    assert receiver_slope_lower > 0
    assert outlow['receiver'][0]-atlow['receiver'] > F(11,1000)
    gap_linear_upper = F(5,6)-(As+package['expense'])-3*(zlo-outside['ell'])
    assert gap_linear_upper < 0
    # The remaining subtracted term (6-p)^2/[6(24-19p)] increases here.
    uniform_gap_lower = (ordinary_combat_bound(p=high,weight=F(3))
                         -athigh['sender']-3*outhigh['receiver'][1])
    assert uniform_gap_lower > F(104,10000)
    return dict(package_sender=package['sender'],package_receiver=package['receiver'],
                outside_sender=outside['sender'],outside_receiver=outside['receiver'],
                ordinary_sender_lower=ordinary_sender_lower,
                uniform_gap_lower=uniform_gap_lower)


def captured_state_bound(*, p, b=F(1), original_receiver=F(0),
                         B=F(1899,10000), damage_s=F(5), damage_r=F(1,100),
                         strength=F(1,20), punishment=F(15), weight=F(8,5)):
    """Note 083 bound, allowing finite destruction after a captured lie."""
    a0=original_receiver
    assert 0 < p < 1 and b >= 1 and 0 <= a0 <= 1
    assert 0 <= strength <= 1 and punishment >= 0
    assert damage_s > 0 and damage_r >= 0
    M=(1-strength)*((1-a0)*(2*b-1-a0)+punishment)
    eta=min(p,p*(damage_s+weight*damage_r)/(damage_s+M))
    assert weight >= 1+eta/(1-p)
    A=(1-p)*(1+weight)+eta
    L=b*(1-p+eta)+weight*a0*(1-p)
    K=b*b+(2*b-1)*eta+weight*a0*a0-L*L/A+(1-weight)*B
    return dict(bound=K,eta=eta,M=M,low_policy=L/A)


def full_budget_package(*,p=F(1,2),a=F(21,50),b=F(1),B=F(1899,10000),
                        f=F(1,1000),costs=(F(1,150),)*3,
                        requests=(F(1,30000),)*3,early_s=F(1,1000),
                        early_r=F(1,1000),update_r=F(1,100)):
    """Full initial transfer: no residual cash quote or quote fee is paid."""
    D=(1-a)**2
    gain=(1-a)*(2*b-1-a)
    mus=[F(0)]*(len(costs)+1)
    for i in reversed(range(len(costs))):
        mus[i]=mus[i+1]+(1-mus[i+1])*requests[i]/D
    q=[1-f/gain]+[1-cost/gain for cost in costs[:-1]]
    Q=F(1); expense=f; false_positive=F(0)
    for mu,qi,ci in zip(mus,q,costs):
        false_positive+=p*Q*mu*(1-qi)/(1-mu)
        Q*=qi
        expense+=Q*ci
    excess=p*D*mus[0]/(1-mus[0])
    sender=(1-p)*(b-a)**2+p*b*b+p*expense+B+early_s
    receiver=((1-p)*a*a+excess+2*a*(1-a)*false_positive-B+early_r+update_r)
    return dict(sender=sender,receiver=receiver,posteriors=mus,q=q,
                expense=expense,false_positive=false_positive,excess=excess,
                C_probability=p*Q,current_receiver=p*a*a+excess)


def audit_renegotiated_family(strength_bound=F(1,20)):
    """Analytical uniform bounds plus endpoint certificates; no grid proof."""
    B,J,rho,ell=F(1899,10000),F(11,1000),F(1,10000),-F(899,5000)
    low,high=F(9,20),F(11,20)
    Dmin=F(2809,10000)
    excess_upper=high*F(1,10000)*F(2809,2808)
    false_upper=high*F(1,2808)*F(43,3000)/Dmin
    receiver_cost_upper=excess_upper+false_upper/2
    assert receiver_cost_upper < F(61,10**6) < rho
    gaps=[]; endpoints=[]
    rounding_cost=F(11,10)*F(1,10**5)+F(11,20)*F(1,10**10)
    for p in (low,high):
        target_squared=ell+(B-J-rho)/(1-p)
        target=sqrt_bounds(target_squared,digits=5)[0]
        assert F(38,100)<target<F(47,100)
        rootlo,_=sqrt_bounds((1-p)*(B-J-rho+(1-p)*ell))
        sender_upper=(1+2*B+F(1,1000)-J-rho+(1-p)*ell
                      -2*rootlo+F(21,1000)*p)
        outside=continuous_outside(p=p)
        bound=captured_state_bound(p=p,strength=strength_bound)
        gap=bound['bound']-sender_upper-F(8,5)*outside['receiver'][1]
        gaps.append(gap)
        package=full_budget_package(p=p,a=target)
        assert package['receiver'] < outside['receiver'][0]
        assert package['sender'] < outside['sender'][0]
        endpoints.append(dict(p=p,target=target,gap=gap,package=package))
    # Note 083 proves concavity of this gap on the entire interval. The
    # lower root bounds make these endpoint margins conservative.
    uniform_gap=min(gaps)-rounding_cost
    assert uniform_gap>(F(649,100000) if strength_bound == 0 else F(8,1000))
    outside=continuous_outside()
    sender_offer=full_budget_package()
    receiver_offer=full_budget_package(a=F(11,50))
    sender_bound=(captured_state_bound(p=F(1,2),strength=strength_bound)['bound']
                  -F(8,5)*outside['receiver'][1])
    receiver_bound=(captured_state_bound(p=F(1,2),weight=F(16,5),strength=strength_bound)['bound']
                    -outside['sender'][1])/F(16,5)
    assert sender_offer['sender']<sender_bound
    assert receiver_offer['receiver']<receiver_bound
    assert sender_offer['receiver']<outside['receiver'][0]
    assert receiver_offer['sender']<outside['sender'][0]
    return dict(uniform_gap_lower=uniform_gap,receiver_cost_upper=receiver_cost_upper,
                endpoints=endpoints,sender_offer=sender_offer,receiver_offer=receiver_offer,
                ordinary_sender_lower=sender_bound,ordinary_receiver_lower=receiver_bound)


def audit_early_goal_repair(early_target=F(1,2)):
    """Note 086's changed disagreement and concave uniform comparison."""
    assert early_target in (F(1,2),F(499,1000))
    B,J,rho=F(1899,10000),F(11,1000),F(1,10000)
    L=early_target**2/2-F(1,5000)
    beta,gamma=F(5,21),F(1,2100)
    receiver_cost=(F(11,20)*F(1,10000)*F(2209,2208)
                   +F(11,20)*F(1,2208)*F(43,3000)/F(2209,10000)/2)
    assert receiver_cost < F(64,10**6) < rho
    assert B>(F(1,2)+L)*gamma/(1+gamma)  # Rational part is concave.
    gaps=[]; endpoints=[]
    for p in (F(9,20),F(11,20)):
        h=1-p
        a=sqrt_bounds(-L+(B-J-rho)/h,digits=5)[0]
        rootlo,_=sqrt_bounds(h*(B-J-rho-h*L))
        sender_upper=p+B+h*(1-L)+B-J-rho-2*rootlo+F(21,1000)*p+F(1,1000)
        multiplier=(h+p*beta)/(h-p*gamma)
        bound=captured_state_bound(p=p,strength=F(0),weight=multiplier)
        r=-h*L
        ordinary_sender=bound['bound']-multiplier*r
        gaps.append(ordinary_sender-sender_upper)
        package=full_budget_package(p=p,a=a)
        assert package['receiver']<r
        assert package['sender']<1+h*(early_target**2-early_target)+F(21,1000)
        endpoints.append(dict(p=p,target=a,package=package,
                              ordinary_sender=ordinary_sender,gap=gaps[-1]))
    rounding=F(11,10)*F(1,10**5)+F(11,20)*F(1,10**10)
    gap=min(gaps)-rounding
    assert gap>(F(25,10000) if early_target==F(1,2) else F(244,100000))
    return dict(uniform_gap_lower=gap,receiver_cost_upper=receiver_cost,endpoints=endpoints)


def ordinary_frontier_at_receiver(r, *,p=F(1,2),B=F(1899,10000),
                                  damage_s=F(5),damage_r=F(1,100),
                                  strength=F(1,20),punishment=F(15)):
    """Certified sharp audit frontier where both payment caps bind (085)."""
    h=1-p; M=(1-strength)*(1+punishment); denominator=damage_s+M
    assert denominator>=1 and M>0
    c=p*damage_r/denominator; A=h+p*damage_s/denominator
    lo,hi=sqrt_bounds((h+c)*(r+B)-c*h)
    xlo,xhi=(c+lo)/(h+c),(c+hi)/(h+c)
    crossing=damage_r/(damage_r+h*M)
    assert crossing<=xlo<=xhi<=F(1,2)
    return dict(policy=(xlo,xhi),
                sender=(p+B+A*(1-xhi)**2,p+B+A*(1-xlo)**2))


if __name__ == '__main__':
    for key,value in audit_funded_witness().items():
        print(key, tuple(float(v) for v in value) if isinstance(value,tuple) else float(value))
    repaired=audit_renegotiated_family()
    for key in ('uniform_gap_lower','receiver_cost_upper','ordinary_sender_lower',
                'ordinary_receiver_lower'):
        print('repaired_'+key,float(repaired[key]))
    print('all_strengths_gap',float(audit_renegotiated_family(F(0))['uniform_gap_lower']))
    print('early_goal_repair_gap',float(audit_early_goal_repair()['uniform_gap_lower']))
