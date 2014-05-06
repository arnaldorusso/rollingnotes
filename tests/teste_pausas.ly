%=============================================
%   	   Created on Frescobaldi
%          Saturday, april, 26. 2014
%=============================================

\version "2.12.0"



#(set-global-staff-size 15)

\header {
    title = "teste_pausas"
    }

\score{
    <<
    \relative c'{
    \set Staff.instrumentName = #"Piano"
    \set Staff.shortInstrumentName = #"Pno."
    \clef treble
    %staffkeysig
    \key c \major 
    %bartimesig: 
    \time 4/4 
    R1  | % 
    r4 r r2      | % 2
    r8 r r r r r r r      | % 3
    c4 d e f      | % 4
    g a b c      | % 5
    d e f g      | % 6
    a b c <c,, c' c'>     | % 7
    c'4 c c8 c c16 c c'8 \bar "|." 
    }% end of last bar in partorvoice
    >>
}