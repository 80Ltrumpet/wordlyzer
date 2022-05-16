# Wordle Analyzer

> A browser-based tool for analyzing Wordle guesses

If you have ever wondered how many words you could have spelled with the
information you received from Wordle, this is for you!

## User Guide

1.  Download the [HTML file](wordlyzer.html) and open it in your web browser.
1.  Type your guesses. No spaces or line breaks are required.
    *   If there is a typo, you can:
        *   Use the backspace key to delete the last cell.
        *   Use the hyphen ("-") key to delete the last row.
        *   Use the escape key to clear all input.
1.  Click on cells to cycle their colors to match your Wordle result.

Every row is labeled on the right with a number that indicates how many words
you could have spelled in the subsequent guess. If you see a red zero, then
the board is in an invalid state. This usually means a cell is not the right
color, yet.

For best results:

*   Only use the analyzer *after* you have completed the puzzle.
*   Do not bother typing the solution word where all five cells are green.
*   Press "Return" or "Enter" to reveal the list of possible words...
    *   ... but only if the number of possibilities is reasonably small.

## Customization

A separate Python script is included in this repository to aid in customization
of the word list used by the analyzer. If you want to use your own word list,
replace the definition of the `DICTIONARY` constant in the HTML file with the
output of the script given your word list as its input.

The HTML file is fully self-contained (i.e., requiring no external resources)
and includes only hand-written HTML 5, CSS, and JavaScript.

## Found a bug?

Please open an issue including the following:

1.  Either a screenshot **OR** a description of the inputs (letters and colors)
and outputs (numbers and, if applicable, list of possible words)
1.  A description of the expected behavior/output.