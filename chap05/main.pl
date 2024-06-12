child(son1, kim).
child(son2, kim).

male(kim).
male(son1).
male(son2).

parent(Y,X) :- child(X,Y).
father(Y,X) :- child(X,Y), male(Y).