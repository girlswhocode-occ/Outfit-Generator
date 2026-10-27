"""Outfit recommendations, grouped by vibe, weather, and occasion."""

OUTFITS = {
    'casual': {
        'hot': {
            'class': (
                'Light linen shorts, a plain cotton tee, and canvas sneakers. Bring a tote '
                'for your notebook.'
            ),
            'hanging out': (
                'A tank or short-sleeve henley, relaxed shorts, slide sandals, and a baseball '
                'cap.'
            ),
            'going out': (
                'A breathable camp-collar shirt, tailored shorts, and clean white sneakers.'
            ),
        },
        'mild': {
            'class': (
                'Straight jeans, a soft crewneck tee, a light denim jacket, and low-profile '
                'sneakers.'
            ),
            'hanging out': (
                'Joggers, a hoodie, and chunky sneakers. Easy layers you can peel off.'
            ),
            'going out': (
                'Dark jeans, a knit polo, a light overshirt, and leather sneakers.'
            ),
        },
        'cold': {
            'class': (
                'Warm sweatpants or thick denim, a long-sleeve tee, a puffer or fleece, and '
                'boots.'
            ),
            'hanging out': (
                'A heavy hoodie, lined joggers, a beanie, and winter sneakers or boots.'
            ),
            'going out': (
                'Dark jeans, a merino sweater, a wool overcoat, and chelsea boots.'
            ),
        },
    },
    'classy': {
        'hot': {
            'class': (
                'Lightweight chinos, a tucked short-sleeve button-up, a slim belt, and '
                'loafers.'
            ),
            'hanging out': (
                'A silk-blend blouse or crisp polo, wide linen trousers, and leather sandals.'
            ),
            'going out': (
                'A linen blazer over a fine tee, tailored shorts or trousers, and suede '
                'loafers.'
            ),
        },
        'mild': {
            'class': (
                'Pressed trousers, a collared shirt, a lightweight cardigan, and oxfords or '
                'loafers.'
            ),
            'hanging out': (
                'A cashmere crewneck, straight trousers, a trench or light coat, and clean '
                'loafers.'
            ),
            'going out': (
                'A tailored blazer, silk shirt or knit, dark trousers, and polished dress '
                'shoes.'
            ),
        },
        'cold': {
            'class': (
                'Wool trousers, a turtleneck, a structured coat, and leather boots.'
            ),
            'hanging out': (
                'A long wool coat, knit dress or trousers with a sweater, tights if you like, '
                'and ankle boots.'
            ),
            'going out': (
                'A tuxedo-adjacent look: black trousers, a satin-trim blazer or wrap coat, '
                'and dress boots.'
            ),
        },
    },
    'bold': {
        'hot': {
            'class': (
                'Color-blocked tee, cargo or graphic shorts, statement sneakers, and a bright '
                'backpack.'
            ),
            'hanging out': (
                'A printed mesh or graphic tank, wide-leg shorts, bold socks, and high-tops.'
            ),
            'going out': (
                'A saturated silk shirt, sharp shorts or a mini skirt, metallic accessories, '
                'and sleek sneakers.'
            ),
        },
        'mild': {
            'class': (
                'A graphic long-sleeve, contrast cargos, a cropped jacket, and loud sneakers.'
            ),
            'hanging out': (
                'A vintage band tee, leather or vinyl jacket, barrel jeans, and platform '
                'boots.'
            ),
            'going out': (
                'A jewel-tone blazer, black trousers or a short dress, stacked jewelry, and '
                'pointed boots.'
            ),
        },
        'cold': {
            'class': (
                'A bright knit under a long coat, dark jeans, a patterned scarf, and combat '
                'boots.'
            ),
            'hanging out': (
                'An oversized graphic hoodie, a statement puffer, wide pants, and chunky '
                'winter boots.'
            ),
            'going out': (
                'A dramatic coat, fitted black layers, a pop of color at the collar or bag, '
                'and heeled boots.'
            ),
        },
    },
}
