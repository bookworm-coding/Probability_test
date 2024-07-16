from modules.format import *


class RDice(Probability):
    def __init__(self, header_text: str, slider_label_text: str, columns1: list[str], columns2: list[str]):
        super().__init__("반복된 주사위 던지기 확률", ":material/ifl:", header_text, slider_label_text, columns1, columns2)
        self.n = st.slider(label="연속 횟수", min_value=2, max_value=10, value=2, step=1, on_change=self.calc)
        self.f = Fraction(1, 6) ** self.n

    def calc(self):
        self.data = [0] * self.length
        randata: list[list[int]] = rand0(6, (self.number, self.n))
        for i in range(self.number):
            if randata[i].count(0) == self.n:
                self.data[0] += 1
            self.result.append(to_fraction(self.data, i + 1))

    def write(self):
        st.write(self.number, "번 주사위를", self.n, "번 던졌을 때 ", 1, "이 연속으로 ", self.n, "번 나올 확률은 ", float(self.result[-1][0]), "이다.")
        st.write("이론상 확률은 ", "$(\\frac{1}{6})^{%d}$" % self.n, "≈", float(self.f), "이다. ")


RDice(
    header_text="주사위를 던졌을 때 1이 N번 연속으로 나올 확률",
    slider_label_text="주사위를 N번 던지는 횟수",
    columns1=["N번 연속 1이 나올 확률"],
    columns2=["N번 연속 1이 나오는 경우의 수"]
).main()
