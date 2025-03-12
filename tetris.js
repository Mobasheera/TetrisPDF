var pixel_fields = [];
var board = new Array(20).fill(0).map(() => new Array(10).fill(0)); // 10x20 grid

function game_init() {
    for (var x = 0; x < 10; ++x) {
        pixel_fields[x] = [];
        for (var y = 0; y < 20; ++y) {
            pixel_fields[x][y] = this.getField(`P_${x}_${y}`);
        }
    }
    console.println("Tetris initialized in PDF!");
}

game_init();

function set_pixel(x, y, state) {
    if (pixel_fields[x] && pixel_fields[x][y]) {
        pixel_fields[x][19 - y].hidden = !state;
    }
}

function handle_input(event) {
    console.println("Key pressed: " + event.change);
    switch (event.change) {
        case 'w': console.println("Rotate!"); break;
        case 'a': console.println("Move Left!"); break;
        case 'd': console.println("Move Right!"); break;
        case 's': console.println("Move Down!"); break;
    }
}

document.onKeyStroke = handle_input;
