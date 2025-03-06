Kurs Mathematik II für Angewandte Informatik: Mehrdimensionale reelle Analysis und numerische Methoden

> Joachim Lammarsch Universität Heidelberg

### Oktober 2024

1/71

# Mehrdimensionale Integration II

In Analogie zum eindimensionalen Fall führt man Riemannsche Zwischensummen für das gesuchte Volumen ein. Dazu definiert man das Volumen eines dreidimensionalen Quaders mit Kantenlängen a, b, c durch

$V:=a\cdot b\cdot c$ (Grandflache $\times$ Hohe)

und unterteilt den Definitionsbereich, d. h. das Rechteck R, durch ein Gitter.

Auf jedem der so entstehenden Teilrechtecke

$$R_{i j}=\left[x_{i-1},x_{i}\right]\times\left[y_{j-1},y_{j}\right].$$

wählt man eine Stelle (*ξ*ij , *η*ij) und berechnet fij := f (*ξ*ij , *η*ij).

# Mehrdimensionale Integration I

Die einfachste mehrdimensionale Integrationsaufgabe entsteht aus dem Problem der Volumenberechnung über Rechtecken. Auf einem ebenen Rechteck R = [a, b] × [c, d] sei eine beschränkte Funktion f : **R** → **R** definiert.

![](_page_0_Figure_13.jpeg)

Zwischen der gewölbten Fläche z = f (x, y ) und R wird ein Volumen V eingeschlossen, welches berechnet werden soll. In der Grafik sieht man links das Volumen unter dem Graphen und rechts ein Rechteckgitter.

2/71

# Mehrdimensionale Integration III

Dann schließt die stückweise konstante Funktion

$${\widehat{f}}\colon R\to\mathbb{R},\quad{\widehat{f}}(x,y)=f_{i j}\ {\mathrm{~{\small~{\mathrm{fur}}~}}}\ (x,y)\in R_{i j}$$

über R das aus Quadern zusammengesetzte Volumen ein:

$$V:=\sum_{i}\sum_{j}f_{i j}\cdot(x_{i}-x_{i-1})\cdot(y_{j}-y_{j-1})$$

# Mehrdimensionale Integration IV

In der Grafik sieht man die Unterteilung eines Volumens und die Approximation durch Quader rechts:

![](_page_1_Figure_2.jpeg)

5/71

# Mehrdimensionale Integration V

### Definition

(a) Es sei R = [a, b] × [c, d] ein Rechteck in der Ebene, f : **R** → **R** eine beschränkte Funktion und Z = {x0, . . . , xn} × {y0, . . . , ym} eine Zerlegung (ein Gitter)

auf R. In jedem Teilrechteck Rij = [xi−1, xi] × [yj−1, yj] sei (*ξ*ij , *η*ij) ein beliebiger Punkt. Dann heißt

$$\sigma(Z):=\sum_{i}^{n}\sum_{j}^{m}f(\bar{\zeta}_{i j},\eta_{i j})(x_{i}-x_{i-1})\cdot(y_{j}-y_{j-1})$$

Zwischensumme von f bezüglich Z.

6/71

# Mehrdimensionale Integration VI

### Definition (Forts.)

(b) Eine Folge von Zerlegungen, für die

$$\operatorname*{max}_{i}\left(\operatorname*{max}_{i}(x_{i}-x_{i-1}),\operatorname*{max}_{j}(y_{j}-y_{j-1})\right)$$

gegen Null strebt, heißt Zerlegungsnullfolge.

- (c) Die reellwertige Funktion f heißt auf (oder über) R (Riemann-)integrierbar, wenn für jede Zerlegungsnullfolge jede Folge von Zwischensummen gegen dieselbe Zahl V strebt.
# Mehrdimensionale Integration VII

### Definition (Forts.) (c) V heißt dann bestimmtes Integral von f über R. Man schreibt dafür V = ZZ R f (x, y ) dxdy Das Integral wird Bereichsintegral, Gebietssintegral, (ebenes) Flächenintegral oder auch Doppelintegral genannt.

In der Literatur werden alternative Schreibweisen wie H R statt RR R verwendet. Ebenso findet man dA, dF oder d(x, y ) für dxdy.

# Mehrdimensionale Integration VIII

Analog zum eindimensionalen Fall können zu einer Zerlegung Z anstatt der Zwischensummen auch Untersummen und Obersummen betrachtet werden:

$$\begin{array}{l l}{{S(Z)=\sum_{i=1}^{n}\sum_{j=1}^{m}(x_{i}-x_{i-1})\operatorname*{inf}_{(x,y)\in R_{i j}}f(x,y)}}\\ {{s(Z)=\sum_{i=1}^{n}\sum_{j=1}^{m}(x_{i}-x_{i-1})\operatorname*{sup}_{(x,y)\in R_{i j}}f(x,y)}}\end{array}$$

Die Funktion f heißt auf R integrierbar, wenn für jede Zerlegungsnullfolge jede Folge von Unter- und Obersummen gegen dieselbe Zahl V strebt.

Der so erhaltene Integralbegriff stimmt mit dem Riemann-Integral überein.

9/71

# Mehrdimensionale Integration IX

Wie im Eindimensionalen ist Beschränktheit notwendig und Stetigkeit hinreichend für Riemann-Integrierbarkeit.

#### Satz

Die reellwertige Funktion f sei auf dem kompakten Rechteck R stetig. Dann ist f über R integrierbar.

Beim Riemann-Integral im eindimensionalen haben wir festgestellt, dass sich der Flächeninhalt unter einem Funktionsgraphen nicht ändert, wenn man eine Funktion f an endlich vielen Stellen umdefiniert oder wenn man statt über das abgeschlossene Intervall [a, b] über das offene Intervall (a, b) oder über eines der halboffenen Intervalle (a, b] und [a, b) integriert.

10/71

# Mehrdimensionale Integration X

Ähnliches gilt auch für mehrdimensionale Integrale. Dazu führen wir den Begriff einer Nullmenge ein.

#### Definition

Eine Teilmenge D des **R**n heißt Nullmenge, wenn es zu jedem *ε* > 0 n-dimensionale Quader gibt, von denen jeder ein positives Volumen besitzt, deren aufsummiertes Volumen höchstens *ε* beträgt und welche D vollständig überdecken.

Eine Teilmenge des **R**n , welche in einem Raum niederer Dimension enthalten ist, ist eine Nullmenge. Anschaulich besitzt eine Nullmenge im **R**2 keinen Flächeninhalt, eine Nullmenge im **R**3 kein Volumen. Teilmengen von Nullmengen sowie Schnitte und Vereinigungen von zwei Nullmengen sind ebenfalls Nullmengen.

# Mehrdimensionale Integration XI

#### Beispiele

- 1 Strecken und Geraden sind Nullmengen im **R**2 (und in allen Räumen höherer Dimension).
- 2 Ebene Flächen sind Nullmengen im **R**3 .
- 3 Die abgeschlossene Einheitskreisscheibe in der (x, y )-Ebene ist eine Nullmenge im **R**3 . Sie ist für beliebiges *ε* > 0 in dem Quader

$$[-1,1]\times[-1,1]\times[-{\frac{\varepsilon}{8}},{\frac{\varepsilon}{8}}]$$

mit Rauminhalt 2 · 2 · *ε* 4 = *ε* enthalten.

# Mehrdimensionale Integration XII

### Doppelintegrale

Die Definition des Integrals im Eindimensionalen kann also für Funktionen in zwei Variablen verallgemeinert werden. Es ist zweckmäßig, sich bewusst zu machen, was dies anschaulich bedeutet. Anstatt die Fläche zwischen x-Achse und Funktion zu bestimmen, fragen wir nun nach dem Volumen zwischen der x-y-Ebene und der Funktion. Für eine formale Definition teilen wir die Funktion in Säulen einer Grundfläche ∆An und Höhe f (xk , yl) ein:

# Mehrdimensionale Integration XIII

### Definition

Sei f : **R**2 → **R** eine stetige Funktion. Sei (ax , ay ),(bx , by ) ∈ **R**2 mit ax < bx und ay < by , ∆xn := (bx−ax ) n und ∆y n := (by−ay ) n . Sei ferner A := [ax , bx ] × [ay , by ] und ∆An := ∆xn · ∆y n . Sei außerdem xk := a + k ∆xn und yl := a + l ∆y n für alle k, l ∈ **N**. Wir definieren das Integral von f über A als

$$\iint_{(A)}f(x,y)\,\mathrm{d}A:=\operatorname*{lim}_{n\to\infty}\left(\sum_{k=1}^{n}\sum_{l=1}^{n}f(x_{k},y_{l})\,\Delta A_{n}\right).$$

13/71

14/71

# Mehrdimensionale Integration XIV

Auch hier gilt wieder, dass der Grenzwert auf der rechten Seite existiert, da f eine stetige Funktion ist. Die im vorherigen Abschnitt beschriebene numerische Berechnung lässt sich leicht auf den mehrdimensionalen Fall verallgemeinern.

# Mehrdimensionale Integration XV

ax

ay

In dieser Situation aber können wir das Integral über A auf zwei eindimensionale Integrale zurückführen, es gilt der Satz von Fubini:

#### Theorem

(A)

Sei f : **R**2 → **R** eine stetige Funktion, (ax , ay ),(bx , by ) ∈ **R**2 mit ax < bx und ay < by und A = [ax , bx ] × [ay , by ]. Dann gilt: ZZ f (x, y ) dA = Z bx Z by f (x, y )dy dx = Z by Z bx f (x, y ) dx dy

Hierbei ist beim sogenannten,,inneren Integral" (das in Klammern) die Integrationsvariable des,,ausseren Integrals" als Konstante zu betrachten. Ansonsten wird wie im Eindimensionalen integriert.  
  

ay

ax

# Mehrdimensionale Integration XVI

Anm.: Eine geschickte Wahl der Reihenfolge der Integration kann manchmal den Aufwand erheblich reduzieren.

![](_page_4_Figure_2.jpeg)

Mehrdimensionale Integration XVII

![](_page_4_Figure_4.jpeg)

17/71

18/71

Mehrdimensionale Integration XVIII

Für kompaktere Notation werden wir künftig

$$\int\limits_{a_{x}}^{b_{x}}\int\limits_{a_{y}}^{b_{y}}f(x,y)\,\mathrm{d}y\,\mathrm{d}x$$

statt R bx ax R by ay f (x, y ) dy ! dx schreiben. Beachten Sie, dass die Reihenfolge von dx und dy die Reihenfolge

der Integration festlegt.

# Mehrdimensionale Integration XIX

Unter Nutzung des Satzes von Fubini kann man viele Rechenregeln für eindimensionale Integrale auf Doppelintegrale übertragen:

#### Beispiele

Es sei f : **R**2 → **R** eine stetige Funktion und (ax , ay ), (bx , by ), (cx , cy ) ∈ **R**2 mit ax < bx < cx und ay < by . Dann gilt beispielsweise: (a) Z bx ax Z by ay f (x, y ) dydx = − Zax bx Z by ay f (x, y ) dydx = − Z bx ax Z ay by f (x, y ) dydx

# Mehrdimensionale Integration XX

![](_page_5_Figure_1.jpeg)

Ein Doppelintegral können wir als Volumen unter einer Funktion auffassen. Bislang können wir aber nur Volumina berechnen, die als Grundfläche ein Rechteck besitzen.

# Mehrdimensionale Integration XXI

Im nächsten Schritt studieren wir, wie man Doppelintegrale über beliebigen Flächen berechnen kann.

Unser Vorgehen ist dabei durch den Satz von Fubini motiviert. Wir betrachten zunächst Flächen, die als Fläche A in der x-y-Ebene zwischen zwei eindimensionalen stetigen Funktionen ga : **R** → **R** und gb : **R** → **R** und den vertikalen Geraden x = a und x = b beschrieben werden können.

Gehört nun der Rand zur Fläche dazu oder nicht? Tatsächlich ist dies egal, denn der Flächeninhalt einer Linie (und damit das darüber liegende Volumen) ist 0, daher stimmen die Werte der Integrale in beiden Fällen überein.

22/71

21/71

Mehrdimensionale Integration XXII

#### Definition

Sei A ⊆ **R**2 die Fläche zwischen zwei stetigen Funktionen ga und gb und Geraden x = a und x = b wie beschrieben. Sei f : **R**2 → **R** eine stetige Funktion. Dann ist das Integral von f über A gegeben durch

$$\iint_{(A)}f(x,y)\,\mathrm{d}A:=\int\limits_{a}^{b}\int\limits_{g_{a}(x)}^{g_{b}(x)}f(x,y)\,\mathrm{d}y\mathrm{d}x.$$

# Mehrdimensionale Integration XXIII

Um Integrale über komplizierteren Flächen betrachten zu können, nutzen wir folgenden Satz:

#### Satz

Sei A = B ⊔ C die disjunkte Vereinigung zweier Flächen in **R**2 und sei f : **R** → **R** eine stetige Funktion. Dann gilt:

$$\iint\limits_{(A)}f(x,y)\,\mathrm{d}A=\iint\limits_{(B)}f(x,y)\,\mathrm{d}A+\iint\limits_{(C)}f(x,y)\,\mathrm{d}A.$$

# Mehrdimensionale Integration XXIV

### Korollar

Sei A = B ∪ C die Vereinigung zweier Flächen in **R**2 und sei f : **R**2 → **R** stetig.

$$\iint\limits_{(A)}f(x,y)\,\mathrm{d}A=\iint\limits_{(B)}f(x,y)\,\mathrm{d}A+\iint\limits_{(C)}f(x,y)\,\mathrm{d}A-\iint\limits_{(B\cap C)}f(x,y)\,\mathrm{d}A.$$

Anm.: Ein Korollar ist in der Mathematik ein mathematischer Satz, der aus einem anderen Satz auf sehr einfache Weise folgt.

Wir können das Korollar hier einfach nachweisen, indem wir das vorherige Theorem auf B ∪ C = (B \ C) ⊔ (B ∩ C) ⊔ (C \ B) anwenden.

25/71

## Anwendungen I

### Flächeninhalte

Wir können Doppelintegrale nutzen, um Flächeninhalte von unregelmäßigen Flächen in der x-y-Ebene zu berechnen. Indem wir die Funktion f , über die Integriert wird, als die konstante Funktion f (x, y ) = 1 wählen. Dann ist der Wert des Volumens über einer Fläche A gleich dem Wert des Flächeninhaltes von A.

# Mehrdimensionale Integration XXV

#### Beispiel

Gegeben eine Fläche A als Teilmenge von **R**2 , die die Form eines "E" ohne Mittelstrich hat, beispielsweise A = ([0, 1] × [0, 3]) ∪ ([1, 2] × [0, 1]) ∪ ([1, 2] × [2, 3]). Wir können dieses A nicht als nach oben und unten durch eine stetige Funktion und nach links und rechts durch eine Gerade begrenzt beschreiben. Sobald wir aber die Fläche A in Teilstücke aufteilen, so können wir über diese jeweils integrieren und dann die Summe betrachten, um das Integral über A zu berechnen.

26/71

## Anwendungen II

#### Beispiel

Es sei A die Fläche zwischen den Funktionen ga(x) = x 4 und gb(x) = x 2 im Bereich x ∈ [0, 1].

Der Wert des Flächeninhalts von A ist dann gleich dem Doppelintegral

$$\begin{split}\iint1\,\mathrm{d}A&=\int\limits_{0}^{1}\int\limits_{\mathbf{g}_{a}(x)}^{\mathbf{g}_{b}(x)}1\,\mathrm{d}y\mathrm{d}x=\int\limits_{0}^{1}\int\limits_{x^{4}}^{x^{2}}1\,\mathrm{d}y\mathrm{d}x\\ &=\int\limits_{0}^{1}\left(x^{2}-x^{4}\right)\,\mathrm{d}x=\frac{1}{3}-\frac{1}{5}=\frac{2}{15}\end{split}$$

## Anwendungen III

Es sei angemerkt, dass wir de facto das eindimensionale Integral über rb(x) − ra(x) berechnen, was anschaulich die Fläche A liefert. Die hier genutzte Methode ist jedoch sehr einfach auf höhere Dimensionen verallgemeinerbar, daher ist sie von großer Praxisrelevanz.

## Anwendungen IV

### Flächenschwerpunkt und Trägheitsmomente

Der Flächenschwerpunkt ist anschaulich der Punkt, auf dem man eine homogene ebene Fläche balancieren könnte.

Wir können seine Koordinaten (xS , yS ) wie folgt bestimmen:

#### Theorem

Sei A eine ebene homogene Fläche. Dann gilt:

$$x_{S}={\frac{1}{A}}\iint\limits_{(A)}x\,\mathrm{d}A\qquad u n d\qquad y_{S}={\frac{1}{A}}\iint\limits_{(A)}y\,\mathrm{d}A$$

Für die Fläche A aus obigen Beispiel, also den Funktionen ga(x) = x 4 und gb(x) = x 2 im Bereich x ∈ [0, 1] erhalten wir beispielsweise (xS , yS ) = 15 2 1 12 , 2 45 = 5 8 , 1 3 .

30/71

29/71

# Anwendungen V

Beachten Sie, dass der Schwerpunkt nicht unbedingt innerhalb von A liegen muss.

Sehr ähnlich wie die Schwerpunktskoordinaten können die Trägheitsmomente einer Fläche bestimmt werden. Diese sind ein Maß für die Widerstandskraft einer Querschnittsfläche gegen das Verbiegens eines Balkens mit ebenjener Querschnittsfläche: Je größer das Trägheitsmoment in entsprechende Richtung, desto mehr Widerstand gegen Biegung in diese Richtung.

## Anwendungen VI

#### Definition

Die Flächenträgheitsmomente in x-, bzw. y-Richtung sind gegeben durch

$$I_{x}=\iint\limits_{(A)}x^{2}\,\mathrm{d}A,\qquad\mathrm{bzw.}\qquad I_{y}=\iint\limits_{(A)}y^{2}\,\mathrm{d}A.$$

## Anwendungen VII

#### Polarkoordinaten

Wenn wir rotationssymmetrische Funktionen oder Flächen betrachten, ist Integration in kartesischen Koordinaten häufig recht umständlich. Man betrachte beispielsweise eine Funktion, die vom Wert 1 im Punkt (0, 0) nach allen Seiten hin mit e −r abfällt, wobei r = p x 2 + y 2 der Abstand vom Punkt (0, 0) ist. Eine solche Funktion ließe sich leicht als Funktion f (r) = e −r beschreiben, doch wenn wir kartesische Koordinaten verwenden (das heißt Punkte in **R**2 Koordinaten (x, y ) zuweisen), hat die Funktion

die kompliziertere Form f (x, y ) = exp − p x 2 + y 2 .

## Anwendungen VIII

Wir werden im Folgenden sehen, wie wir auf konsistente Weise Funktionen in zwei Variablen mit Hilfe von r statt mittels (x, y ) beschreiben und dadurch Integration rotationssymmetrischer Probleme erheblich vereinfachen können.

34/71

33/71

## Anwendungen IX

Betrachten wir einen Punkt ⃗x ∈ **R**2 , so haben wir dessen Position bislang immer dadurch beschrieben, dass wir seine Verschiebung in x- und y-Richtung vom Koordinatenursprung angegeben haben, also ⃗x = (x, y ). Wir könnten die Position von ⃗x aber ebenfalls dadurch festlegen, dass wir den Abstand vom Koordinatenursprung r und den Winkel *θ*, den die Strecke zwischen ⃗x und dem Koordinatenursprung einschließen, angeben, also ⃗x = (r, *θ*). Um sicherzustellen, dass diese Beschreibung eindeutig ist, fordern wir r ≥ 0 und 0 ≤ *θ* < 2*π*. Wir nennen (r, *θ*) die Polarkoordinaten und (x, y ) die kartesischen Koordinaten von ⃗x.

## Anwendungen X

Beachten Sie, dass sich nicht der Punkt ⃗x selbst ändert, sondern nur unsere Beschreibung seiner Position.

#### Theorem

Für den Übergang von kartesischen zu Polarkoordinaten und umgekehrt gilt:

$$\begin{array}{l l}{{x=r\,\cos(\theta)}}&{{\qquad}}\\ {{r=\sqrt{x^{2}+y^{2}}}}&{{\qquad}}\\ {{\qquad}}&{{\theta=\arctan\left(\frac{y}{x}\right)}}\end{array}$$

## Anwendungen XI

Wir können unter Nutzung dieses Theorems Funktionen statt mittels kartesischen Koordinaten nun alternativ mit Polarkoordinaten beschreiben. Es ist wichtig, sich klar zu machen, dass sich die Funktion (z. B. als Fläche im **R**3 ) nicht ändert, sondern wir sie nur anders beschreiben.

37/71

Anwendungen XIII

Der Nutzen von Polarkoordinaten ist, dass wir bestimmte Funktionen oder Flächen auf diese Weise sehr viel kompakter beschreiben können. Wir können dann sogar unter Nutzung von Polarkoordinaten integrieren und erhalten dasselbe Ergebnis wie bei Integration mit kartesischen Koordinaten, insbesondere ist das Volumen unter der Funktion natürlich gleich geblieben.

## Anwendungen XII

#### Beispiel

Es sei f (x, y ) = x 2 − y 2 . Dann können wir f im Polarkoordinaten schreiben als:

$f(r,\theta)=(r\,\cos(\theta))^{2}-(r\,\sin(\theta))^{2}=r^{2}\left(\cos^{2}(\theta)-\sin^{2}(\theta)\right).$

Wir können partielle Ableitungen von f nach r und *θ* betrachten, beispielsweise ist

$${\frac{\partial f}{\partial r}}(r,\theta)=2r\left(\cos^{2}(\theta)-\sin^{2}(\theta)\right).$$

Anm.: Wir verwenden ja immer schon die Schreibweise sink (*θ*) für (sin(*θ*)) k für beliebige k, ebenso für alle anderen trigonometrischen Funktionen.

38/71

## Anwendungen XIV

Die gegebenenfalls kompaktere Form der Funktion kann die Integration dabei ganz erheblich erleichtern. Formal gilt:

#### Theorem

Sei f : **R**2 → **R** eine stetige Funktion und sei A = {(r, *θ*) ∈ **R**2 | ga(*θ*) ≤ r ≤ gb(*θ*)}, wobei ga, gb : [0, 2*π*) → **R** stetige Funktionen sind. Dann gilt:

$\int f(r,\theta)\mathrm{d}A=\int\int f(r,\theta)\,r\mathrm{d}r\,\mathrm{d}\theta$

## Anwendungen XV

Dies kann man als Analogon zur Definition mit kartesischen Koordinaten sehen.

Anm.: Der Satz über die Integration mittels disjunkter Vereinigung zweier Flächen ist selbstverständlich auch hier weiter gültig; ebenfalls läßt sich der Satz von Fubini anwenden, sofern die Integrationsgrenzen konstant sind.

Der zusätzliche Faktor r im Integral ist die Determinante der Jacobi-Matrix, auch genannt Jacobi-Determinante. Wann immer wir die Integrationsvariablen von kartesischen Koordinaten zu Polarkoordinaten wechseln muss dieser Faktor hinzugefügt werden.

Das folgende Beispiel zeigt die einfache Integration in Polarkoordinaten, viel schwieriger wäre direktes Integrieren in kartesischen Koordinaten gewesen (probieren Sie es aus)!

41/71

## Anwendungen XVI

#### Beispiel

Wir wollen das Integral

$$\int\limits_{-1}^{1}{\sqrt{1-y^{2}}}\,\int\limits_{0}^{y}{\frac{y}{\sqrt{x^{2}+y^{2}}}}\,\mathrm{d}x\mathrm{d}y$$

berechnen. Dafür sind kartesische Koordinaten gänzlich ungeeignet, denn zum einen ist der Nenner des Integranden gerade der Abstand vom Koordinatenursprung r und zum anderen ist die Fläche, über die integriert wird, der Halbkreis

$A=\{(r,\theta)\in\mathbb{R}^{2}\mid r\leq1,-\frac{\pi}{2}\leq\theta\leq\frac{\pi}{2}\}$ .  
  

42/71

## Anwendungen XVII

### Beispiel (Forts.)

Wir führen daher eine Transformation zu Polarkoordinaten durch:

$$\int\limits_{-1}^{1}\int\limits_{0}^{1}\frac{y}{\sqrt{x^{2}+y^{2}}}\,\mathrm{d}x\mathrm{d}y=\int\limits_{0}^{1}\int\limits_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\frac{r\sin(\theta)}{r}\,r\,\mathrm{d}\theta\mathrm{d}r$$
 
$$=\int\limits_{0}^{1}r\,\left(-\cos\left(\frac{\pi}{2}\right)+\cos\left(\frac{\pi}{2}\right)\right)\,\mathrm{d}r=0,$$

Beachten Sie das Auftreten der Determinante der Jacobi-Matrix im zweiten Term. Das Integral wurde durch zwei aufeinander folgende eindimensionale Integrationen gelöst.

## Anwendungen XVIII

#### Dreifachintegrale

Der Integrationsbegriff auf Funktionen in drei Dimensionen bedeutet Dreifachintegrale zu betrachten.

Aus den Definitionen von Integration in zwei und drei Variablen sollte dann klar sein, wie man im allgemeinen Fall von Funktionen in n Variablen vorgeht. Da solche Fälle aber in der Praxis quasi keine Relevanz besitzen, werde ich hier darauf nicht weiter eingehen.

## Anwendungen XIX

Formal könnte man bei der Definition von Dreifachintegralen wieder den Grenzwert gewisser Summen betrachten, wir wollen hier jedoch vom dreidimensionalen Satz von Fubini ausgehen:

## Anwendungen XX

#### Theorem

Sei f : **R**3 → **R** eine stetige Funktion, seien (ax , ay , az ),(bx , by , bz ) ∈ **R**3 mit ax < bx , ay < by und az < bz und sei V = [ax , bx ] × [ay , by ] × [az , bz ]. Dann gilt:

$$\iiint_{(V)}f(x,y,z)\,\mathrm{d}V=\iint_{a_{x}}\int\limits_{a_{y}}\int\limits_{a_{z}}f(x,y,z)\,\mathrm{d}z\mathrm{d}y\mathrm{d}x.$$

Dabei ist die Reihenfolge der Integrationsvariablen vertauschbar.

45/71

46/71

## Anwendungen XXI

Analog zu Doppelintegralen, dürfen die Integralgrenzen der inneren Integrale auch von den äußeren Integrationsvariablen abhängen, die Vertauschung der Integrationsvariablen ist nicht mehr uneingeschränkt möglich.

## Anwendungen XXII

#### Beispiel

Es sein R := [0, 2] × [0, 1] × [0, 1] ein Quader mit Kantenlängen 2, 1 und 1 sowie f : R → **R**, f (x, y, z) = 1 + xy + z. Dann folgt

$$\begin{split}\iint\limits_{(R)}f(x,y,z)\,\mathrm{d}R&=\iiint\limits_{(R)}f(x,y,z)\,\mathrm{d}x\mathrm{d}y\mathrm{d}z\\ &=\int\limits_{z=0}^{1}\left(\int\limits_{y=0}^{1}\left(\int\limits_{z=0}^{2}\left(1+xy+z\right)\mathrm{d}x\right)\mathrm{d}y\right)\mathrm{d}z\\ &=\int\limits_{z=0}^{1}\left(\int\limits_{y=0}^{1}\left[x+\frac{1}{2}x^{2}y+xz\right]_{x=0}^{2}\mathrm{d}y\right)\mathrm{d}z\end{split}$$

## Anwendungen XXIII

$$\iint\limits_{(R)}f(x,y,z)\,\mathrm{d}R=\int\limits_{z=0}^{1}\left(\int\limits_{y=0}^{1}(2+2y+2z)\mathrm{d}y\right)\mathrm{d}z$$
 
$$=\int\limits_{z=0}^{1}\left[\left(2y+y^{2}+2yz\right)\right]_{y=0}^{1}\mathrm{d}z$$
 
$$=\int\limits_{z=0}^{1}(2+1+2z)\,\mathrm{d}z$$
 
$$=\left[\left(3z+z^{2}\right)\right]_{z=0}^{1}=4$$

49/71

## Anwendungen XXIV

### Beispiel

Sei V = {(x, y, z) ∈ **R**3 | 0 ≤ x ≤ 1, 0 ≤ y ≤ (1 − x), 0 ≤ z ≤ 1 − (x + y )}. Dabei ist A die Menge aller Punkte in **R**3 mit positiven Koeffizienten, die die Ungleichung x + y + z ≤ 1 erfüllen.

V wird durch die Koordinatenebenen sowie die, durch die drei Punkte (1, 0, 0), (0, 1, 0) und (0, 0, 1) aufgespannte Ebene, berandet.

Wir wollen nun die Funktion f (x, y, z) = xyz über V integrieren. Das Ergebnis hat keine gute Anschauung.

50/71

## Anwendungen XXV

### Beispiel (Forts.)

Wir berechnen hier das vierdimensionale Volumen zwischen der Funktion und dem durch die Koordinatenachsen gegebenen dreidimensionalen Raum, es geht dabei um das formale Vorgehen:

$$\begin{split}\iint f(x,y,z)\,\mathrm{d}V&=\int\limits_{0}^{1}\int\limits_{0}^{1-x}\int\limits_{0}^{1-x-y}f(x,y,z)\,\mathrm{d}z\mathrm{d}y\mathrm{d}x\\ &=\int\limits_{0}^{1}\int\limits_{0}^{1-x}\int\limits_{0}^{1-x-y}xyz\,\mathrm{d}z\mathrm{d}y\mathrm{d}x\end{split}$$

## Anwendungen XXVI

### Beispiel (Forts.)

Wie im Falle von Doppelintegralen haben wir hier das Dreifachintegral als drei eindimensionale Integrationen geschrieben, bei denen wir die jeweils anderen Variablen als konstant ansehen.

## Anwendungen XXVII

Wir betrachten nun zuerst die Integration über z:

$$\int\limits_{0}^{1-x-y}x y z\mathrm{d}z=\left[{\frac{x y z^{2}}{2}}\right]_{0}^{1-x-y}={\frac{1}{2}}x y(1-x-y)^{2}.$$

Wir können dieses Ergebnis nun in die obige Gleichung einsetzen und erhalten:

$$\iiint\limits_{(A)}f(x,y,z)\,\mathrm{d}A=\int\limits_{0}^{1}\int\limits_{0}^{1-x}{\frac{1}{2}}x y(1-x-y)^{2}\,\mathrm{d}y\mathrm{d}x.$$

Beachten Sie, dass nach der Integration über z diese Variable nicht mehr auftaucht.

53/71

## Anwendungen XXVIII

Als nächstes betrachten wir die Integration über y:

$$\int\limits_{0}^{1-x}xy(1-x-y)\,\mathrm{d}y=\left[\frac{1}{2}xy^{2}-\frac{1}{2}x^{2}y^{2}-\frac{1}{3}xy^{3}\right]_{0}^{1-x}$$
 
$$=\frac{1}{2}x(1-x)^{2}-\frac{1}{2}x^{2}(1-x)^{2}-\frac{1}{3}x(1-x)^{3}$$

Dies setzen wir nun wieder in die vorherige Gleichung ein, und erhalten:

$$\iiint\limits_{(A)}f(x,y,z)\,\mathrm{d}A=\int\limits_{0}^{1}\left({\frac{1}{2}}x(1-x)^{2}-{\frac{1}{2}}x^{2}(1-x)^{2}-{\frac{1}{3}}x(1-x)^{3}\right)\,\mathrm{d}x$$

54/71 Beachten Sie, wie nach Integration über y diese Variable nicht mehr auftritt.

## Anwendungen XXIX

Es verbleibt eine eindimensionale Integration über x:

ZZZ (A) f (x, y, z) dA = Z 1 0 1 2 x(1 − x) 2 − 1 2 x 2 (1 − x) 2 − 1 3 x(1 − x) 3 dx = Z 1 0 1 2 (x − 2x 2 + x 3 ) − 1 2 (x 2 − 2x 3 + x 4 ) − 1 3 (x − 3x 2 + 3x 3 − x 4 ) dx

Anwendungen XXX

$$=\int\limits_0^1\left({\frac{1}{6}}x-{\frac{1}{2}}x^{2}+{\frac{1}{2}}x^{3}-{\frac{1}{6}}x^{4}\right)\,\mathrm{d}x$$
 
$$=\left[{\frac{1}{12}}x^{2}-{\frac{1}{6}}x^{3}+{\frac{1}{8}}x^{4}-{\frac{1}{30}}x^{5}\right]_0^1$$
 
$$={\frac{1}{12}}-{\frac{1}{6}}+{\frac{1}{8}}-{\frac{1}{30}}={\frac{1}{120}}$$

## Anwendungen XXXI

### Volumen, Schwerpunkt und Trägheitsmomente

Ganz in Analogie zur Berechnung von Flächeninhalten mit Doppelintegralen kann mittels Dreifachintegralen das Volumen eines beliebig geformten Körpers berechnet werden.

Sei dazu ein Körper V geeignet parametrisiert, das heißt beispielsweise, dass für geeignete a, b ∈ **R** mit a < b und stetige Funktionen ga, gb : **R** → **R** sowie ha, hb : **R**2 → **R** gilt

> V = (x, y, z) ∈ **R** 3 | a ≤ x ≤ b ga(x) ≤ y ≤ gb(x) ha(x, y ) ≤ z ≤ hb(x, y )}

> > 57/71

## Anwendungen XXXII

Dann gilt für das Volumen von V, das wir ebenfalls mit V bezeichnen wollen, dass

$$V=\iiint\mathbf{1}\,\mathrm{d}V$$
 
$$(V)$$
 
$$=\int\int\int\mathbf{1}\,\mathrm{d}z\mathrm{d}y\mathrm{d}x.$$

58/71

## Anwendungen XXXIII

Für den Schwerpunkt (xS , yS , zS ) ∈ **R**3 eines homogenen Körpers V gilt

$$x_{\mathcal{S}}={\frac{1}{V}}{\iint}{\iint}x\,\mathrm{d}V$$
 
$$(V)$$
 
$$y_{\mathcal{S}}={\frac{1}{V}}{\iint}{\iint}y\,\mathrm{d}V$$
 
$$(V)$$
 
$$z_{\mathcal{S}}={\frac{1}{V}}{\iint}{\iint}z\,\mathrm{d}V$$
 
$$(V)$$

Anwendungen XXXIV

Im zweidimensionalen war der Schwerpunkt einer Fläche derjenige Punkt, auf dem man diese Fläche balancieren könnte. Im dreidimensionalen ist der Schwerpunkt derjenige Punkt, an dem bei Angreifen einer beliebigen Kraft nur Beschleunigung, aber keine Rotation erzeugt wird. So ist der Schwerpunkt einer Kugel beispielsweise ihr Zentrum.

## Anwendungen XXXV

Einen dritter Anwendungsfall von Dreifachintegralen bilden Trägheitsmomente.

Obwohl die Formeln für Trägheitsmomente hier ähnlich den Formeln für Flächenträgheitsmomente im Zweidimensionalen sind, haben sie eine völlig andere Interpretation:

Während Flächenträgheitsmomente die Widerstandskraft gegen Verformung beschreiben, geben die Trägheitsmomente im Dreidimensionalen ein Maß für den Widerstand eines Körpers V gegen eine Änderung seiner Drehgeschwindigkeit um die entsprechende Koordinatenachse.

Anm.: Eine andere Art sich dies vorzustellen ist, dass der physikalisch erhaltene Drehimpuls L das Produkt aus Trägheitsmoment und Drehgeschwindigkeit ist.

61/71

## Anwendungen XXXVI

Es gilt für die Trägheitsmomente in Richtung der Koordinatenachsen (m die Masse und V das Volumen des Objektes):

$$I_{\mathrm{x}}={\frac{m}{V}}{\iint}{\iint}(y^{2}+z^{2})\mathrm{d}V$$
   
 
$$\begin{array}{l}{(V)}\\ {I_{\mathrm{y}}={\frac{m}{V}}{\iint}{\iint}(x^{2}+z^{2})\mathrm{d}V}\\ {(V)}\\ {I_{\mathrm{z}}={\frac{m}{V}}{\iint}{\iint}(x^{2}+y^{2})\mathrm{d}V}\\ {(V)}\end{array}$$

62/71

# Zylinder- und Kugelkoordinaten I

Bei der Berechnung von Doppelintegralen ist aufgefallen, dass manche Probleme in Polarkoordinaten (r, *θ*) deutlich besser zu lösen sind, als in den üblichen kartesischen Koordinaten (x, y ). Bei der Berechnung von Dreifachintegralen treten solcherart Probleme ebenfalls auf, weshalb es nützlich ist, Alternativen zu den dreidimensionalen kartesischen Koordinaten (x, y, z) zur Verfügung zu haben. Wir werden hier zwei dieser Alternativen kennen lernen: Zylinder- und Kugelkoordinaten.

# Zylinder- und Kugelkoordinaten II

Zylinderkoordinaten sind Polarkoordinaten sehr ähnlich: Statt einen Punkt ⃗x ∈ **R**3 mittels kartesischer Koordinaten ⃗x = (x, y, z) zu beschreiben, nutzen wir in der x-y-Ebene Polarkoordinaten (r, *θ*) und behalten die z-Koordinate einfach bei. Mit anderen Worten, wie schreiben ⃗x = (r, *θ*, z) mit r ≥ 0 und 0 ≤ *θ* < 2*π*.

# Zylinder- und Kugelkoordinaten III

Die Umrechnung von kartesischen Koordinaten in Zylinderkoordinaten erfolgt analog zu oben. Zylinderkoordinaten sind von großem Nutzen bei der Betrachtung von Objekten, die um eine Achse rotieren.

Die Determinante der Jacobi-Matrix ist hier dieselbe wie im Falle von Polarkoordinaten, also ein Faktor r.

65/71

# Zylinder- und Kugelkoordinaten V

Kugelkoordinaten sind sehr gut für kugelsymmetrische Probleme geeignet. Beispielsweise könnte eine Fragestellung sein, die elektrische Ladung einer Metallkugel bei gegebener Ladungsdichte zu bestimmen.

Weder kartesische, noch Zylinderkoordinaten sind gut geeignet, um ein Dreifachintegral über eine Kugel zu bestimmen. Die Idee hinter Kugelkoordinaten ist sehr ähnlich zur Idee hinter Polarkoordinaten: Man verwende Winkel um die Position eines Punkte zu beschreiben statt Verschiebungen vom Koordinatenursprung aus.

# Zylinder- und Kugelkoordinaten IV

Es gilt:

### Theorem

Sei f : **R**3 → **R** stetig und V = {(r, *θ*, z) ∈ **R**3 | a ≤ z ≤ b, ga(*θ*, z) ≤ r ≤ gb(*θ*, z)} wobei ha, hb : [0, 2*π*) × [a, b] → **R** stetige Funktionen sind und a, b ∈ **R** mit a < b. Dann gilt:

ZZZ (V ) f (r, *θ*, z)dV = Z b a Z 2*π* 0 hb(*θ*,z) Z ha(*θ*,z) f (r, *θ*, z)rdrd*θ*dz

66/71

Zylinder- und Kugelkoordinaten VI

Sei ⃗x = (x, y, z) ∈ **R**3 ein Punkt. Wir berechnen die Kugelkoordinaten von ⃗x wie folgt:

Theorem (Kartesisch2Kugelkoordinaten)

Für den Übergang von kartesischen Koordinaten zu Kugelkoordinaten (r, *ϕ*, *θ*) gilt

x = r cos(*ϕ*) sin(*θ*) y = r sin(*ϕ*) sin(*θ*) z = r cos(*θ*).

Es gilt dabei r ≥ 0, 0 ≤ *ϕ* < 2*π* und 0 ≤ *θ* ≤ *π* und r = p x 2 + y 2 + z 2.

# Zylinder- und Kugelkoordinaten VII

Anschaulich ist *ϕ* der Winkel zwischen der x-z-Ebene und der Ebene, die die z-Achse und den Punkt ⃗x enthält. Der Winkel *θ* ist der Winkel zwischen der Verbindungslinie von Koordinatenursprung zu ⃗x und der z-Achse. Zuletzt ist r der Abstand von Koordinatenursprung zum Punkt ⃗x.

Wichtig festzuhalten dabei ist, dass dies nicht dasselbe r wie für Polar- und Zylinderkoordinaten ist! Man mache sich bewusst, dass Kugelkoordinaten eindeutig die Position eines Punkts in **R**3 beschreiben: Ausgehend vom Koordinatenursprung legt der Winkel *ϕ* eine Richtung in der x-y-Ebene fest und der Winkel *θ* gibt gewissermaßen eine Steigung an. Damit wissen wir durch (*ϕ*, *θ*), in welcher Richtung vom Koordinatenursprung der Punkt ⃗x liegt. Damit wissen wir aber auch, wo ⃗x liegt, denn r gibt die Entfernung vom Koordinatenursprung an.

# Zylinder- und Kugelkoordinaten VIII

![](_page_17_Figure_4.jpeg)

70/71

69/71

# Zylinder- und Kugelkoordinaten IX

Bei Integration in Kugelkoordinaten gilt:

#### Theorem

Sei f : **R**3 → **R** eine stetige Funktion und V = {(r, *ϕ*, *θ*) ∈ **R**3 | ha(*ϕ*, *θ*) ≤ r ≤ hb(*ϕ*, *θ*)} wobei ha, hb : [0, 2*π*) × [0, *π*] → **R** stetige Funktionen sind. Dann gilt:

$$\iiint_{(V)}f(r,\phi,\theta)\mathrm{d}V=\int\limits_{0}^{\pi}\int\limits_{0}^{2\pi}\int\limits_{h_{\phi}(\phi,\theta)}f(r,\phi,\theta)\;r^{2}\sin(\theta)\;\mathrm{d}r\mathrm{d}\phi\mathrm{d}\theta.$$

Beachten Sie das Auftreten der Jacobi-Determinante r 2 sin(*θ*).