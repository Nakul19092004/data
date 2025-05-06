data = [2, 4, 10, 12, 3, 20, 30, 11, 25] 
 
# Initial centroids 
m1 = 2 
m2 = 4 
 
for _ in range(10):  # max 10 iterations 
    g1 = [] 
    g2 = [] 
 
    # Assign to nearest cluster 
    for x in data: 
        if abs(x - m1) < abs(x - m2): 
            g1.append(x) 
        else: 
            g2.append(x) 
     
    # Recalculate means 
    new_m1 = sum(g1) / len(g1) 
    new_m2 = sum(g2) / len(g2) 
 
    # Stop if centroids don’t change 
    if new_m1 == m1 and new_m2 == m2: 
        break 
     
    m1 = new_m1 
    m2 = new_m2 
 
# Final output 
print("Cluster 1:", g1) 
print("Cluster 2:", g2) 
print("Final Centroids:", round(m1, 2), "and", round(m2, 2)) 
