def format_by_template(input_str: str, template: str) -> str:
    len_template: int = len(template)
    if len(input_str) <= 1 or len_template <= 1:
        return input_str
    result: list[str] = []
    temp_index: int = 0
    good_added_count: int = 0
    for symbol in input_str:
        if symbol == template[temp_index] and good_added_count < len_template:
            if temp_index < len_template - 1:
                temp_index += 1
            result.append(symbol)
            good_added_count += 1
        else:
            result.append("*")
    return "".join(result)


def test_simple():
    input_str: str = "soooommmmeeeee"
    template: str = "some"
    expected: str = "so***m***e****"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_long_dublicate():
    input_str: str = "foooooooo"
    template: str = "fo"
    expected: str = "fo*******"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_long_dublicate_reverse():
    input_str: str = "ooooooooooooooof"
    template: str = "of"
    expected: str = "o**************f"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_two_correct():
    input_str: str = "fullllll"
    template: str = "full"
    expected: str = "full****"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_three_correct():
    input_str: str = "fullllll"
    template: str = "fulll"
    expected: str = "fulll***"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_dublicated_symbols_is_correct():
    input_str: str = "ffffuuull_stttaaaccck"
    template: str = "full_stack"
    expected: str = "f***u**ll_st**a**c**k"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_not_all_dublicated_symbols_is_correct():
    input_str: str = "ffffuuulll_stttaaaccck"
    template: str = "full_stack"
    expected: str = "f***u**ll*_st**a**c**k"
    result: str = format_by_template(input_str, template)
    assert result == expected


def test_without_duplicates():
    input_str: str = "ststononltltieie"
    template: str = "stone"
    expected: str = "st**on*******e**"
    result: str = format_by_template(input_str, template)
    assert result == expected
