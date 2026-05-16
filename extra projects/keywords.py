def process_signals(signals):
    total_checked = 0
    
    for signal in signals:
        total_checked += 1
        
        if signal == "RED":
            print("Stop")
            break
            
        elif signal == "YELLOW":
            continue
            
        elif signal == "GREEN":
            pass
            
    return total_checked

signal_list = ["GREEN", "YELLOW", "GREEN", "RED", "GREEN"]
checked_count = process_signals(signal_list)
print(checked_count)