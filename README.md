# Procedurally Generated Sudoku Puzzles

This program actually does a couple things. In addition to procedurally generating a sudoku puzzle that (in theory) is always solvable, it also uses Python Turtle to display the puzzle. Lastly, in whatever directory your script is in, it creates a new sudoku.pdf file with the most recent puzzle, which is ready for printing!

I used recursion and a backtracking algorithm to both generate the original "filled" board and create the final puzzle to be solved. By checking the puzzle each time a value is removed, we ensure that no unsolvable sudoku boards are created by mistake.

This took me an evening to write, which is much faster than I expected and I'm really happy with the results. Once I got in the zone it was a pretty seamless experience. Plus, there's a fair amount of resources online about backtracking and procedural key/lock generation, so it was easy to answer any of my questions that came up. Honestly, the most time consuming part was using Turtle, as I haven't used it before and wanted to explore other graphics in Python, and learning how to convert the created canvas into a .pdf file was a pain but super interesting!

I'd love to explore procedural generation more in the future, especially around level design, but I'm also interested in enemy design and have done some code already on different forms of 2D world generation (hoping to add that here in the future). It's such an interesting study and is becoming more tightly connected with AI design in video games, so it's an exciting prospect as well!
