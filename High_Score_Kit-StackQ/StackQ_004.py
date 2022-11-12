def solution(bridge_length, weight, truck_weights):
    time = 0
    time_stack = []
    on_bridge = []
    while len(on_bridge) > 0 or len(truck_weights) > 0:
        if len(time_stack) > 0:
            if (time_stack[0] + bridge_length) == time:
                on_bridge.pop(0)
                time_stack.pop(0)

        if len(on_bridge) < bridge_length and sum(on_bridge) < weight:
            if len(truck_weights) > 0:
                if sum(on_bridge) + truck_weights[0] <= weight:
                    on_bridge.append(truck_weights.pop(0))
                    time_stack.append(time)

        time += 1
        print("time: ",time_stack)
        print("bridge: ",on_bridge)


    return time



# print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))