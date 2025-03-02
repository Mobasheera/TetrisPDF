var pixel_fields = [];

function game_init() {
    // Gather references to pixel field objects
    for (var x = 0; x < 10; ++x) {
        pixel_fields[x] = [];
        for (var y = 0; y < 20; ++y) {
            pixel_fields[x][y] = this.getField(`P_${x}_${y}`);
        }
    }
}

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
