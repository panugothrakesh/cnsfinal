def rail_fence_encrypt(message, num_rails):
    rails = [[] for _ in range(num_rails)]
    rail_index, direction = 0, 1
    for char in message:
        rails[rail_index].append(char)
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1
    return ''.join(''.join(rail) for rail in rails)


def rail_fence_decrypt(ciphertext, num_rails):
    rail_pattern = [[] for _ in range(num_rails)]
    rail_index, direction = 0, 1
    for _ in ciphertext:
        rail_pattern[rail_index].append('*')
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1
    index = 0
    for rail in rail_pattern:
        for j in range(len(rail)):
            rail[j] = ciphertext[index]
            index += 1
    rail_index, direction = 0, 1
    decrypted_message = []
    for _ in ciphertext:
        decrypted_message.append(rail_pattern[rail_index].pop(0))
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1
    return ''.join(decrypted_message)


message = "HELLOTHISISRAILFENCE"
num_rails = 3
encrypted = rail_fence_encrypt(message, num_rails)
print(f"Encrypted: {encrypted}")
decrypted = rail_fence_decrypt(encrypted, num_rails)
print(f"Decrypted: {decrypted}")