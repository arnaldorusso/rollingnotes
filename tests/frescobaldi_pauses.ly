\version "2.16.2"

\header {
  title = "Pauses test"
}

global = {
  \key c \major
  \time 4/4
}

right = \relative c'' {
  \global
  % Music follows here.
    R1  | % 
    r4 r r2      | % 2
    r8 r r r r r r r      | % 3
    c,4 d e f      | % 4
    g a b c      | % 5
    d e f g      | % 6
    a b c <c,, c' c'>     | % 7
    c'4 c c8 c c16 c c'8 \bar "|." 
  
}

\score {
  \new PianoStaff <<
    \new Staff = "right" \with {
      midiInstrument = "acoustic grand"
    } \right
  >>
  \layout { }
  \midi {
    \context {
      \Score
      tempoWholesPerMinute = #(ly:make-moment 100 4)
    }
  }
}
