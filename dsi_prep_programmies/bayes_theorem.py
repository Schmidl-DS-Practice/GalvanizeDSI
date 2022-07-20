#P(A | B) = (P(B | A) * P(A)) / P(B)
#P(B) = P(A)*P(B|A) + P(not A)*P(B|not A)

def bayes_two(Pba, Pa, Pbna, Pna ):
    # ONLY TWO CONDITIONS MEANS A AND NOT A
    Pb = (Pa * Pba) + (Pna * Pbna)
    return (Pba * Pa) / Pb

def bayes_three(Pba, Pa, Pba1, Pa1, Pba2, Pa2, Pba3, Pa3 ):
    Pb = (Pba1 * Pa1) + (Pba2 * Pa2) + (Pba3 * Pa3)
    return (Pba * Pa) / Pb

def main():
    # BOTH BAYES
    Pba = .55
    Pa = .35
    # BAYES TWO
    Pbna = 0.4
    Pna = .65
    # BAYES THREE
    Pba1 = .55
    Pa1 = .35
    Pba2 = .35
    Pa2 = .4
    Pba3 = .79
    Pa3 = .25

    posterior1 = bayes_two(Pba, Pa, Pbna, Pna)
    #print(posterior1)

    posterior2 = bayes_three(Pba, Pa, Pba1, Pa1, Pba2, Pa2, Pba3, Pa3)
    print(posterior2)

if __name__ == "__main__":
    main()
