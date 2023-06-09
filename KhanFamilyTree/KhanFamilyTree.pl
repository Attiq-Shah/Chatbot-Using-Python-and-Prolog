mianbiwi('Chote Khan', 'Choti Rani').
mianbiwi('Barre Khan', 'Barri Rani').
mianbiwi('Nadir', 'Nahid').
mianbiwi('Asad', 'Sumra').
mianbiwi('Salim', 'Kausar').
mianbiwi('Rizwan', 'Sanam').

parent('Chote Khan', 'Kausar').
parent('Chote Khan', 'Nadir').
parent('Chote Khan', 'Asad').
parent('Choti Rani', 'Kausar').
parent('Choti Rani', 'Nadir').
parent('Choti Rani', 'Asad').

parent('Barre Khan', 'Nahid').
parent('Barre Khan', 'Sumra').
parent('Barri Rani', 'Nahid').
parent('Barri Rani', 'Nahid').

parent('Nadir', 'Burhan').
parent('Nadir', 'Rashid').
parent('Nadir', 'Akram').

parent('Nahid', 'Burhan').
parent('Nahid', 'Rashid').
parent('Nahid', 'Akram').

parent('Asad', 'Salima').
parent('Asad', 'Sanam').
parent('Sumra', 'Salima').
parent('Sumra', 'Sanam').

parent('Salim', 'Rizwan').
parent('Kausar', 'Rizwan').

parent('Rizwan', 'Rabia').
parent('Sanam', 'Rabia').

gins('mard', 'Chote Khan').
gins('mard', 'Barre Khan').
gins('mard', 'Salim').
gins('mard', 'Nadir').
gins('mard', 'Asad').
gins('mard', 'Rizwan').
gins('mard', 'Burhan').
gins('mard', 'Rashid').
gins('mard', 'Akram').

gins(aurat, 'Choti Rani').
gins(aurat, 'Barri Rani').
gins(aurat, 'Kausar').
gins(aurat, 'Nahid').
gins(aurat, 'Sumra').
gins(aurat, 'Salima').
gins(aurat, 'Sanam').
gins(aurat, 'Rabia').

baap(Variable1, Variable2):-
    parent(Variable1, Variable2),gins(mard, Variable1).

maa(Variable1, Variable2):-
    parent(Variable1, Variable2),gins(aurat, Variable1).


beti(V1, V2):-
    parent(V2, V1), gins(aurat, V1).

beta(V1, V2):-
    parent(V2, V1), gins(mard, V1).

dada(V1, V2):-
    parent(X, V2), gins(mard, X), gins(mard, V1),parent(V1, X).

nana(V1, V2):-
    parent(X, V2), gins(aurat, X), gins(mard, V1), parent(V1, X).

dadi(V1, V2):-
    parent(X, V2), gins(mard, X), gins(aurat, V1),parent(V1, X).

nani(V1, V2):-
    parent(X, V2), gins(aurat, X), gins(aurat, V1), parent(V1, X).

behn(V1, V2):-
    parent(X, V1),gins(mard, X), parent(X, V2), gins(aurat, V1), not(V1=V2).

bhai(V1, V2):-
    parent(X, V1), gins('mard', X), parent(X, V2), gins('mard', V2), not(V1=V2).

sala(V1, V2):-
    behn(X, V2), mianbiwi(V1, X).

bahu(V1, V2):-
    parent(V2, X), mianbiwi(X, V1).

pota(V1, V2):-
    dada(V2, V1); dadi(V2, V1), gins('mard', V1).

poti(V1, V2):-
    dada(V2, V1); dadi(V2, V1), gins('aurat', V1).

sussar(V1, V2):-
    mianbiwi(X, V2), parent(V1, X), gins('mard', V1).

saas(V1, V2):-
    mianbiwi(X, V2), parent(V1, X), gins(aurat, V1).

chachataya(V1, V2):-
    parent(X, V2), gins('mard', X), bhai(X, V1), gins('mard', V1).

khala(V1, V2):-
    parent(X, V2), gins('aurat', X), behn(X, V1), gins('aurat', V1).

baapdada(X, Y):-
    parent(X, Y), gins('mard', X).
baapdada(X, Y):-
    parent(X, Z), baapdada(Z, Y), gins('mard', Z), gins('mard', X).

nawasa(V1,V2):-
    nani(V2, V1); nana(V2, V1), gins('mard', V1).

nawasi(V1,V2):-
    nani(V2, V1); nana(V2, V1), gins(aurat, V1).

firstelem(First, List):-
    List = [H|_], First = H.












