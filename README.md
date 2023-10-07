# Making flashcards for piano

Transcribe a song into the lilypond format. The [Lilypond Learning Manual](https://lilypond.org/doc/v2.23/Documentation/learning/index) will help
you with this. Also available in [PDF form](https://lilypond.org/doc/v2.24/Documentation/learning.pdf).

Once transcribed, make sure you got it right by running

```
lilypond <your-file.pdf>
```

and verifying the output. Here is a useful development tip: while in vim run `autocmd BufWritePost * silent !lilypond -l NONE <your-file>.ly` and then open up `zathura` in a separate window. This will refresh the pdf every time you make a change and then save.

Once done grab that stuff and throw it into the `generate-flashcards.py` template.
You will almost certainly have to modify the template a bit to work with your
own special weird stuff. But after messing with it you can print and cut things
out and you are ready to start practicing.
