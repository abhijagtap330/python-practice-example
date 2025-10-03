def simple_interest(principal:int, interest:float, time:float):
    
    apply = (principal * interest * time) / 100
    
    return apply

print(simple_interest(10000,15,10))

def compund_interest(principal, rate, times_compounded, time):
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * time)
    # Calculate the compound interest
    compound_interest = amount - principal
    return compound_interest
