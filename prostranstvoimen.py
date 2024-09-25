calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    a = tuple(str(len(string)))
    return a, string.upper(), string.lower()

def is_contains(str, list_to_search):
    count_calls()
    if str in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cycle'])) # No matches
print(calls)