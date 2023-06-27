with open('./text.txt','w+') as file:
    for line in file:
        print(line)
    file.write('\n nuevas cosas')
    file.write('\n orale')
    file.write('\n orale')