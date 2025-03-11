console.log("Script loaded!");

var pixel_fields = [];

const game_init = () => {
    console.log("game_init called!");
    for (var x = 0; x < 10; ++x) {
        pixel_fields[x] = [];
        for (var y = 0; y < 20; ++y) {
            pixel_fields[x][y] = this.getField("P_" + x + "_" + y);
        }
    }
};

// Call game_init automatically when the PDF opens
game_init();

function set_pixel(x, y, state) {
    // Show or hide pixel based on state (true = visible, false = hidden)
    pixel_fields[x][20 - 1 - y].hidden = !state;
}

function handle_input(event) {
    switch (event.change) {
        case 'w': rotate_piece(); break;
        case 'a': move_left(); break;
        case 'd': move_right(); break;
        case 's': lower_piece(); break;
    }
}

function rotate_piece() {
    console.log("Rotate piece");
}

function move_left() {
    console.log("Move left");
}

function move_right() {
    console.log("Move right");
}

function lower_piece() {
    console.log("Lower piece");
}