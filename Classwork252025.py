def main():
    n = int(input().strip()) #Здесь пишите кол-во городов
    m = int(input().strip()) #Здесь пишите кол-во дорог

    graph = [[] for _ in range(n + 1)] #массив графов
    for _ in range(m): #цикл
        a,b,w = map(int, input().split()) #читаем города А и Б, а также вес
        graph[a].append((b, w)) #теперь это однонаправленная дорога

    s, t = map(int, input().split()) #

    #массив максимальной пропускной способности до каждого города
    best = [0] * (n + 1)
    best[s] = float('inf')  #начальный город имеет неограниченную пропускную способность

    #а теперь обработаем эту сучку
    queue = [(s, best[s])]  #спосок пар (пара не пара)

    while queue:
        # находим элемент который может сделать максимум пропусков
        max_index = 0
        for i in range(1, len(queue)):
            if queue[i][1] > queue[max_index][1]:
                max_index = i

        #достаем этот элемент
        u, cur_cap = queue.pop(max_index)

        # Если закончилось, то кончилось
        if u == t:
            print(cur_cap)
            return

        #обрабатываем все дороги из города u
        for v, w in graph[u]:
            new_cap = min(cur_cap, w)  # Ограничение на пути - минимум из текущего значения и дороги
            if new_cap > best[v]:  #если нашли лучший путь до v, обновляем
                best[v] = new_cap
                queue.append((v, new_cap))  #добавляем в очередь для обработки

    #если путь до t не найден, выводим 0
    print(0)

if __name__ == "__main__": #запускание программы
    main()