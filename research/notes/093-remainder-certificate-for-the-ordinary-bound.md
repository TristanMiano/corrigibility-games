# A complete remainder certificate for the ordinary comparison

**R0004 proof audit; analytical self-check.** This expands the algebra
behind 079 and 083, including the original receiver's offset and its
actual combat expense. The certificate identifies exactly which slack
conditions must vanish for the stated stronger control to attain the
bound.

Let h=1-p, 0<p<1, b>=1, and 0<=a_0<=1. Conditional on type t, let
m_t=E[Y|t], q_t=E[Y^2|t], sender physical expense C_t>=0, receiver
physical expense V_t>=0 and net payment t_t from S to R. Require
0<=Y<=1 and t_0,t_1<=B. Define

\[
d=C_1+t_1-C_0-t_0-2b(m_1-m_0)+(q_1-q_0).
\]

The capture law must actually supply d>=-M w_1,
C_1>=d_S w_1 and V_1>=d_R w_1. These are coupling/physical premises,
not consequences of the algebra. For 083's main a_0=0 class,
M=(1-s)(2b-1+P_max); using a larger valid M only weakens the bound.

Take 0<=eta<=p, lambda>=1+eta/h, and
(p-eta)d_S+lambda p d_R-eta M>=0. Put

\[
\begin{aligned}
A_0&=h(1+\lambda)+\eta,&
L_0&=b(h+\eta)+\lambda a_0h,&x_0&=L_0/A_0,\\
A_1&=p(1+\lambda)-\eta,&
H&=p(b+\lambda a_0)-(b-1)\eta,\\
\alpha_0&=h(\lambda-1)-\eta,&
\alpha_1&=p(\lambda-1)+\eta.
\end{aligned}
\]

Here H>=p(1+lambda*a_0)>0, A_0,A_1>0, and both alphas are
nonnegative. Original losses are

\[
\begin{aligned}
L_S={}&h(q_0-2bm_0+b^2+C_0+t_0)\\
&+p(q_1-2(b+1)m_1+(b+1)^2+C_1+t_1),\\
L_R={}&h(q_0-2a_0m_0+a_0^2+V_0-t_0)\\
&+p(q_1-2(1+a_0)m_1+(1+a_0)^2+V_1-t_1).
\end{aligned}
\]

For
K=b^2+(2b-1)eta+lambda*a_0^2-L_0^2/A_0+(1-lambda)B,
the following is an exact identity:

\[
\begin{aligned}
L_S+\lambda L_R-K={}&
A_0(q_0-m_0^2)+A_1(q_1-m_1^2)+A_0(m_0-x_0)^2\\
&+(1-m_1)\{A_1(1-m_1)+2H\}\\
&+(h+\eta)C_0+\lambda h V_0\\
&+(p-\eta)C_1+\lambda p V_1+\eta d\\
&+\alpha_0(B-t_0)+\alpha_1(B-t_1).
\tag{1}
\end{aligned}
\]

To derive it, subtract eta*d from the weighted losses. The low-policy
quadratic has coefficients A_0 and -2L_0. Complete its square. The
high-policy quadratic has coefficient A_1 and its derivative at 1
is -2H, so expand about that upper endpoint. The remaining payment
coefficients are -alpha_0,-alpha_1, whose sum is 1-lambda.
The remaining constants simplify to the stated K.

All terms in (1) are nonnegative after grouping its high cost-and-IC
line:

\[
(p-\eta)C_1+\lambda pV_1+\eta d
\ge[(p-\eta)d_S+\lambda p d_R-\eta M]w_1\ge0.
\]

Thus L_S+lambda L_R>=K. A low minimizer x_0 outside [0,1] still
gives a valid (looser) lower bound; x_0 in the physical interval is
required for the attaining construction, not for the inequality itself.

At an interior audit-dominant eta=p(d_S+lambda*d_R)/(d_S+M), the cost
coefficient vanishes. Equality uses deterministic low policy x_0,
high policy 1, exact capture IC, no extra on-path burns, and the full
payments when their alpha coefficients are positive. At alpha_0=0,
lower low-state payments can remain on the supporting line, giving
085's adjacent segment. If lambda*d_R>=M, eta=p is admissible and
ordinary money burning supplies the alternative frontier. Positive
setup expenses or extra verification work add slack; an algebraically
attaining free controller must be labeled as that stronger control.

This certificate covers arbitrary finite communication satisfying the
coupling premises through its induced moments and expenses. It does
not assume that the displayed two-report menu is the only permitted
ordinary mechanism. Protected direct state evidence, useful capture,
new productive output and different funding laws require new premises.
