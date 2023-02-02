from pelangiApp.pelangi import Rainbow,CompleteRainbow,Sky,MockRainbow

def test_should_return_normal_merah_kuning_hijau_after_paint():
    rainbow = Rainbow()
    rainbow.paint_this_rainbow()
    colors = rainbow.get_all_color()
    expected = ['merah', 'kuning', 'hijau']
    assert colors == expected

def test_paint_this_rainbow_complete():
    rainbow = CompleteRainbow()
    rainbow.paint_this_rainbow()
    colors = rainbow.get_all_color()
    expected = ['merah', 'jingga', 'kuning', 'hijau', 'biru', 'nila', 'ungu']
    assert colors == expected  

def test_append_rainbow_with_mock_rainbow():
    sky = Sky()
    fake_rainbow = MockRainbow()
    sky.append_rainbow(fake_rainbow)
    rainbows = sky.get_all_rainbow()
    expected = [fake_rainbow]
    assert expected == rainbows

