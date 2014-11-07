\version "2.18.0"

\header {
  title = ""
}

global = {
  \time 4/4
  \key c \major
}


melody = \relative c'' {
  \global
  c4 d e f
  R1  | % 
  r4 r r2      | % 2
  r8 r r r r r r r      | % 3
  c4 d e f      | % 4
  g a b c      | % 5
  d e f g      | % 6
  a b c <c,, c' c'> \bar "|."     | % 7
  c'4 c c8 c c16 c c'8 \bar "|."  

}

words = \lyricmode {
  
  
}
