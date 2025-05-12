import math

PI = math.pi
FLUID_TO_CUBIC_INCH = 1.805 

def fluid_volume_cubic_inches(volume_oz):
    return volume_oz * FLUID_TO_CUBIC_INCH

def inside_radius(volume_cubic_in, height):
    return math.sqrt(volume_cubic_in / (PI * height))

def outer_radius(inner_radius, thickness):
    return inner_radius + thickness

def outer_height(height, thickness):
    return height + thickness

def glass_weight(inner_r, outer_r, full_height, density):
    volume = PI * full_height * (outer_r**2 - inner_r**2)
    return volume * density  

def box_arrange():
    options = []
    for r in range(1, 13):
        for c in range(1, 13):
            for s in range(1, 13):
                if r * c * s == 12:
                    options.append((r, c, s))
    return options

def box_dimensions(opt_arrangement, diameter, height):
    rows, cols, stacks = opt_arrangement
    return (cols * diameter, rows * diameter, stacks * height)

def box_volume(length, width, height):
    return length * width * height

def best_box(arrangements, diameter, height):
    best = None
    min_vol = float('inf')

    for arr in arrangements:
        l, w, h = box_dimensions(arr, diameter, height)
        vol = box_volume(l, w, h)
        if vol < min_vol:
            min_vol = vol
            best = (arr, (l, w, h))

    return best

def read_glasses(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                yield map(float, line.strip().split())

def main():
    for volume, height, density, thickness in read_glasses("test.txt"):
        print(f"\nGlass Specs:\n  Volume: {volume} oz\n  Height: {height} in\n  Density: {density} oz/in³\n  Thickness: {thickness} in")

        vol_cubic = fluid_volume_cubic_inches(volume)
        r_inner = inside_radius(vol_cubic, height)
        r_outer = outer_radius(r_inner, thickness)
        h_outer = outer_height(height, thickness)

        glass_oz = glass_weight(r_inner, r_outer, h_outer, density)
        glass_lb = glass_oz / 16  
        total_weight = 12 * glass_lb

        arrangements = box_arrange()
        best_arr, (L, W, H) = best_box(arrangements, 2 * r_outer, h_outer)

        print(f"\nBest arrangement (rows × cols × stacks): {best_arr}")
        print(f"Box dimensions (L x W x H): {L:.2f} x {W:.2f} x {H:.2f} inches")
        print(f"Total weight of 12 glasses: {total_weight:.2f} lbs")

if __name__ == "__main__":
    main()
