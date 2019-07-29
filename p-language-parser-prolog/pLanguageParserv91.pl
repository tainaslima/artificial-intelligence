
% Author: Tainá Lima
% Description: Verifies if a portguese phrase is in fact a portuguese phrase.
% If so, translate a portuguese phrase, given as a list of word, to a P language phrase, vice versa.
% Date: 22.06.2019

% Database
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel(á).
vowel(í).
vowel(ó).
vowel(ú).

consonant(b).
consonant(c).
consonant(d).
consonant(f).
consonant(g).
consonant(h).
consonant(j).
consonant(k).
consonant(l).
consonant(m).
consonant(n).
consonant(p).
consonant(q).
consonant(r).
consonant(s).
consonant(t).
consonant(v).
consonant(x).
consonant(y).
consonant(z).

articleF([a|S]-S).
articleF([as|S]-S).
articleF([uma|S]-S).
articleF([umas|S]-S).

articleM([o|S]-S).
articleM([os|S]-S).
articleM([um|S]-S).
articleM([uns|S]-S).

pronounF([eu|S]-S).
pronounF([tu|S]-S).
pronounF([ela|S]-S).
pronounF([nós|S]-S).
pronounF([vós|S]-S).
pronounF([elas|S]-S).

pronounM([eu|S]-S).
pronounM([tu|S]-S).
pronounM([ele|S]-S).
pronounM([nós|S]-S).
pronounM([vós|S]-S).
pronounM([eles|S]-S).

possessivePronounF([meu|S]-S).
possessivePronounF([teu|S]-S).
possessivePronounF([dela|S]-S).
possessivePronounF([nosso|S]-S).
possessivePronounF([delas|S]-S).

possessivePronounM([meu|S]-S).
possessivePronounM([teu|S]-S).
possessivePronounM([dele|S]-S).
possessivePronounM([nosso|S]-S).
possessivePronounM([deles|S]-S).

adjectiveF([bonita|S]-S).
adjectiveF([linda|S]-S).
adjectiveF([feia|S]-S).
adjectiveF([esplendorosa|S]-S).
adjectiveF([diva|S]-S).
adjectiveF([inteligente|S]-S).
adjectiveF([modelo|S]-S).
adjectiveF([ícone|S]-S).
adjectiveF([fria|S]-S).

adjectiveM([bonito|S]-S).
adjectiveM([lindo|S]-S).
adjectiveM([feio|S]-S).
adjectiveM([esplendoroso|S]-S).
adjectiveM([divo|S]-S).
adjectiveM([inteligente|S]-S).
adjectiveM([modelo|S]-S).
adjectiveM([ícone|S]-S).
adjectiveM([frio|S]-S).

nounF([gata|S]-S).
nounF([mulher|S]-S).
nounF([casa|S]-S).
nounF([cadela|S]-S).
nounF([porta|S]-S).
nounF([escova|S]-S).
nounF([menina|S]-S).

nounM([gato|S]-S).
nounM([homem|S]-S).
nounM([casebre|S]-S).
nounM([cachorro|S]-S).
nounM([porteiro|S]-S).
nounM([pente|S]-S).
nounM([menino|S]-S).

verb([sou|S]-S).
verb([és|S]-S).
verb([é|S]-S).
%verb([e|S]-S).
verb([somos|S]-S).
verb([sóis|S]-S).
verb([são|S]-S).

verb([estou|S]-S).
verb([estás|S]-S).
verb([está|S]-S).
verb([estamos|S]-S).
verb([estais|S]-S).
verb([estão|S]-S).

verb([amo|S]-S).
verb([amas|S]-S).
verb([ama|S]-S).
verb([amamos|S]-S).
verb([amais|S]-S).
verb([amam|S]-S).

% Given a phrase in portuguese, represented as a list of words, verifies if this list is, in fact, a portuguese phrase.

phrase(S) :- subjectF(S-S1), predicateF(S1-[]).
phrase(S) :- subjectM(S-S1), predicateM(S1-[]).

subjectF(S) :- subjectCoreF(S).
subjectF(S-S0) :- articleF(S-S1), subjectCoreF(S1-S0).

subjectM(S) :- subjectCoreM(S).
subjectM(S-S0) :- articleM(S-S1), subjectCoreM(S1-S0).

subjectCoreF(S-S0) :- adjectiveF(S-S1), subjectCoreF(S1-S0).
subjectCoreF(S-S0) :- possessivePronounF(S-S1), subjectCoreF(S1-S0).
subjectCoreF(S) :- nounF(S).
subjectCoreF(S) :- pronounF(S).
subjectCoreF([]-[]).

subjectCoreM(S-S0) :- adjectiveM(S-S1), subjectCoreM(S1-S0).
subjectCoreM(S-S0) :- possessivePronounM(S-S1), subjectCoreM(S1-S0).
subjectCoreM(S) :- nounM(S).
subjectCoreM(S) :- pronounM(S).
subjectCoreM([]-[]).

predicateF(S-S0) :- verb(S-S1), objectF(S1-S0).
predicateF(S) :- verb(S).

predicateM(S-S0) :- verb(S-S1), objectM(S1-S0).
predicateM(S) :- verb(S).

objectF(S-S0) :- articleF(S-S1), objectCoreF(S1-S0).
objectF(S) :- objectCoreF(S).

objectCoreF(S-S0) :- adjectiveF(S-S1), objectCoreF(S1-S0).
objectCoreF(S-S0) :- possessivePronounF(S-S1), objectCoreF(S1-S0).
objectCoreF(S) :- nounF(S).
objectCoreF(S) :- pronounF(S).
objectCoreF([]-[]).

objectM(S-S0) :- articleM(S-S1), objectCoreM(S1-S0).
objectM(S) :- objectCoreM(S).
objectCoreM(S-S0) :- adjectiveM(S-S1), objectCoreM(S1-S0).
objectCoreM(S-S0) :- possessivePronounM(S-S1), objectCoreM(S1-S0).
objectCoreM(S) :- nounM(S).
objectCoreM(S) :- pronounM(S).
objectCoreM([]-[]).

% Given two words Xs and Ys, represented by a list of syllables, verifies if Ys is Xs written in P language.

concat([], Ys, Ys).
concat([X|Xs], Ys, [X|Zs]) :- concat(Xs, Ys, Zs).

checkSyllable([X], [X,p,X]).
checkSyllable([X|Xs], [X|Ys]):- consonant(X), checkSyllable(Xs,Ys).
checkSyllable([X|Xs], Ys) :- vowel(X), concat([X],Xs, Ss), concat([p], Ss,Ts), concat(Ss, Ts,Ys).

isPWord([],[]).
isPWord([X|Xs], [Y|Ys]) :- string_chars(X,Xss),  checkSyllable(Xss,Yss), string_chars(Y,Yss), isPWord(Xs,Ys).

% Given two words Xs and Ys, represented by a list of syllables, verifies if Ys is Xs written in portuguese.

membro(X,[X|Xs]).
membro(X, [Y|Xs]) :- membro(X,Xs).

contem([],Ys).
contem([X|Xs],Ys) :- membro(X,Ys), contem(Xs,Ys).

checkSyllableP([p|Xs], [p|Ys]) :- contem([p],Xs), checkSyllableP(Xs,Ys).
checkSyllableP([X|Xs],[X|Ys]) :- X \== p, checkSyllableP(Xs,Ys).
checkSyllableP([p|Xs], []) :- not(contem([p],Xs)).

isPortWord([],[]).
isPortWord([X|Xs],[Y|Ys]) :- string_chars(X,Xss),  checkSyllableP(Xss,Yss), string_chars(Y,Yss), isPortWord(Xs,Ys).

% For every portuguese word in phrase list, convert it to P language
translate([], []).
translate([X|Xs], [Y|Ys]) :- isPWord(X,Y), translate(Xs, Ys).

% For every P language word in phrase list, convert it to portuguese
translate2([], []).
translate2([X|Xs], [Y|Ys]) :- isPortWord(X,Y), translate2(Xs, Ys).

% For every word, represented as a list of syllables, concat theses syllables to form a word (string)
createStringString([],[]).
createStringString([X|Xs], [Y|Ys]) :- atomics_to_string(X,Y), createStringString(Xs,Ys).

% For every word, represented as a string, concat theses string, using space as separator, to form a phrase (string)
createString(Xs, Y) :- createStringString(Xs,Zs), atomics_to_string(Zs,' ',Y).

translateToP(Xs,Ys) :- translate(Xs,Zs), createString(Zs,Ys).

translateToPort(Xs,Ys) :- translate2(Xs,Zs), createString(Zs,Ys).

% For every string in the entry list, convert it to atom
cleanQuotations([],[]).
cleanQuotations([X|Xs],[Y|Ys]) :- atom_string(Y,X), cleanQuotations(Xs,Ys).

% Main rules
mainP(Xs,Zs, Ks) :- createStringString(Xs,Ys),cleanQuotations(Ys,Ss), phrase(Ss), translate(Xs,Zs),createString(Zs,Ks).
mainPort(Xs,Zs, Ys):- translate2(Xs,Ys), createStringString(Ys,Ss), cleanQuotations(Ss,Ts),phrase(Ts), createString(Ys,Zs).

% Input example:
% mainPort([["opo"], ["capa", "chorpor", "ropo"], ["épé"], ["bopo", "nipi", "topo"]],Ss, Ks)
%  MainP([ [o],[ca, chor, ro], [é] , [bo,ni,to] ], Zs, Ks)
