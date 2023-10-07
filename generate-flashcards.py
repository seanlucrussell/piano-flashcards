#!/usr/bin/python3

left = [
   "\clef bass d8 <a fis'>-. a, <a fis'>-. b, <a fis'>-. cis <a fis'>-. "
   , "\clef bass d8 <a fis'>-. a, <a fis'>-. b, <a fis'>-. cis <a fis'>-. "
   , "\clef bass d8 <a fis'>-. a, <a fis'>-. b, <a fis'>-. cis <a fis'>-. "
   , "\clef bass e8 <b g'>-. b, <b g'>-. cis <cis' g'>-. a, <cis' g'>-. "
   , "\clef bass b,8 <b fis'>-. bes, <b fis'>-. a, <b fis'>-. aes, <b fis'>-. "
   , "\clef bass g,8 <b g'>-. g, <b g'>-. a, <cis' a'>-. a, <cis' a'>-. "
   , "\clef bass d8 <a fis'>-. a, <a fis'>-. b, <a fis'>-. cis <a fis'>-. "
   , "\clef bass e8 <b g'>-. b, <b g'>-. cis <cis' g'>-. a, <cis' g'>-. "
   , "\clef bass b,8 <b fis'>-. bes, <b fis'>-. a, <b fis'>-. aes, <b fis'>-. "
   , "\clef bass g,8 <b g'>-. g, <b g'>-. a, <cis' a'>-. a, <cis' a'>-. "
   , "\clef treble g8-. <b' d''>-. d-. <b' d''>-. g-. <b' d''>-. d-. <b' d''>-. "
   , "\clef treble a8-. <e' cis''>-. e-. <e' e''>-. a-. <e' cis''>-. a-. aes-. "
   , "\clef treble g8-. <g' b'>-. e-. <g' b'>-. g-. fis-. g-. gis-. "
   , "\clef treble a8-. <a' cis''>-. e-. <a' cis''>-. a-. <a' cis''>-. e-. <a' cis''>-. "
   , "\clef treble g8-. <b' d''>-. d-. <b' d''>-. g-. <b' d''>-. d-. <b' d''>-. "
   , "\clef treble a8-. <e' cis''>-. e-. <e' e''>-. a-. <e' cis''>-. a-. aes-. "
   , "\clef treble g8-. <g' b'>-. e-. <g' b'>-. g-. fis-. g-. gis-. "
   , "\clef treble a8-. <a' cis''>-. e-. <a' cis''>-. a-. <a' cis''>-. \clef bass a, cis "
   ]

right = [
   "\clef treble r1 "
   , "\clef treble r2 r4. fis''16 g'' "
   , "\clef treble a''8-. a''-. a''16 g'' fis'' g'' a''4 d'''8 e''16 fis'' "
   , "\clef treble g''8-. g''-. g''16 fis'' e'' fis'' g''4 d'''8 d''16 e'' "
   , "\clef treble fis''8-. fis''-. fis''16 e'' d'' e'' fis''8-. b''-. d'''-.  b''-. "
   , "\clef treble g''4-! b'8-. d''-. cis''-. d''-. e''-. fis''16 g'' "
   , "\clef treble a''8-. a''-. a'' \prall fis''16 g'' a''4 d'''8 e''16 fis'' "
   , "\clef treble g''8-. g''-. g'' \prall e''16 fis'' g''4 cis'''8 d''16 e'' "
   , "\clef treble fis''8-. fis''-. fis'' \prall d''16 e'' fis''8-. b''-. cis'''-.  d'''-. "
   , "\clef treble e'''8-. b''-. b''16 d''' \\acciaccatura {cis'''8 d'''8} d'''8 e'''-. fis'''-. g'''4 "
   , "\clef treble r8 b''-. cis'''-. d'''-. cis'''-. b''-. a''-. gis''-. "
   , "\clef treble a''4-! b''8-. r16 b''16 cis'''2 "
   , "\clef treble r8 b''8 cis'''-. d'''-. e'''-. b''-. cis'''-. d'''-. "
   , "\clef treble cis'''4-! b''8-. \\acciaccatura cis''' d'''16 b'' a''2 "
   , "\clef treble r8 b'' cis'''-. d'''-. cis'''-. b'' \prall a''-. gis''-. "
   , "\clef treble a''16 e'' a'' b'' cis''' b'' cis''' d''' e'''2 "
   , "\clef treble r8 b'' cis'''-. d'''-. e'''-. d''' \prall cis'''-. b''-. "
   , "\clef treble cis'''8-. a''-. a''16 gis'' a'' b'' cis''' b'' cis''' d''' e'''4"
   ]

key = "\key d \major"
print ('\\version "2.22.1"')
print ('\header { tagline = " " }')
print ('\paper {print-page-number = ##f }')

for i in range(len(right)):
    print ('\markup ' + str(i + 1) + ' \\new PianoStaff <<')
    print ('  \\new Staff {')
    print ('    \key d \major')
    print('    ' + right[i] + '|' )
    print('    ' + right[(i+1) % len(right)] + '|' )
    print('    ' + right[(i+2) % len(right)] + '|' )
    print ('  }')
    print ('  \\new Staff {')
    print ('    \key d \major')
    print('    ' + left[i] + '|' )
    print('    ' + left[(i+1) % len(left)] + '|' )
    print('    ' + left[(i+2) % len(left)] + '|' )
    print ('  }')
    print ('>>')
