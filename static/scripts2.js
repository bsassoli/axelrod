function makeGrid(n, l) {
    var c = document.getElementById("verifica");
    c.innerText = String(lattice)
    
    var grid = document.getElementById("grid");
    for (var rows = 0; rows < size; rows++) {
        var currentRow = grid.insertRow(rows);
        for (var col = 0; col < size; col++) {
            var currentCell = currentRow.insertCell(col);
            /* currentCell.innerText = JSON.parse(lattice)[rows][col];*/
            currentCell.style.width = '40px';
            currentCell.style.height = '40px';
            currentCell.style.border = "2px solid black";
        }
    }
}
makeGrid(size, lattice);