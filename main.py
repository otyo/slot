import pyxel


class App:
    def __init__(self):
        pyxel.init(56, 80, caption="slot")
        pyxel.load("assets/spic.pyxres")
        self.coin = 100
        self.len_1 = [1, 1, 2, 4, 3, 4, 2, 3, 0, 1]
        self.len_2 = [0, 4, 2, 1, 2, 1, 3, 4, 3, 1]
        self.len_3 = [0, 1, 2, 3, 0, 1, 2, 4, 3, 0]
        self.len_y1 = [-9, 0, 9, 18, 27, 36, 45, 54, 63, 72]
        self.len_y2 = [-9, 0, 9, 18, 27, 36, 45, 54, 63, 72]
        self.len_y3 = [-9, 0, 9, 18, 27, 36, 45, 54, 63, 72]
        self.stop = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.t = 0
        self.c1 = 1
        self.c2 = 1
        self.c3 = 1
        self.ok1 = 1
        self.ok2 = 1
        self.ok3 = 1
        self.x = 15
        self.y = 16
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y
        self.mb = pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)
        self.p = 1
        pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.mouse(True)
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y
        if self.ok1 == 1:
            for y1 in range(10):
                self.len_y1[y1] += 1

        for y in range(10):
            if self.len_y1[y] >= 81:
                self.len_y1[y] = -9

        if self.ok2 == 1:
            for y2 in range(10):
                self.len_y2[y2] += 1

        for y in range(10):
            if self.len_y2[y] >= 81:
                self.len_y2[y] = -9
        if self.ok3 == 1:
            for y3 in range(10):
                self.len_y3[y3] += 1

        for y in range(10):
            if self.len_y3[y] >= 81:
                self.len_y3[y] = -9

        if self.my <= 55 and 49 <= self.my and self.mx <= 23 and 17 <= self.mx and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.c1 = 0
        if self.my <= 55 and 49 <= self.my and self.mx <= 31 and 25 <= self.mx and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.c2 = 0
        if self.my <= 55 and 49 <= self.my and self.mx <= 39 and 33 <= self.mx and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.c3 = 0

        if self.c1 == 0 and self.len_y1[0] % 9 == 0:
            self.ok1 = 0
            for a in range(10):
                if self.len_y1[a] == 0:
                    self.stop[0][0] = self.len_1[a]
                if self.len_y1[a] == 9:
                    self.stop[0][1] = self.len_1[a]
                if self.len_y1[a] == 18:
                    self.stop[0][2] = self.len_1[a]

        if self.c2 == 0 and self.len_y2[0] % 9 == 0:
            self.ok2 = 0
            for b in range(10):
                if self.len_y2[b] == 0:
                    self.stop[1][0] = self.len_2[b]
                if self.len_y2[b] == 9:
                    self.stop[1][1] = self.len_2[b]
                if self.len_y2[b] == 18:
                    self.stop[1][2] = self.len_2[b]

        if self.c3 == 0 and self.len_y3[0] % 9 == 0:
            self.ok3 = 0
            for c in range(10):
                if self.len_y3[c] == 0:
                    self.stop[2][0] = self.len_3[c]
                if self.len_y3[c] == 9:
                    self.stop[2][1] = self.len_3[c]
                if self.len_y3[c] == 18:
                    self.stop[2][2] = self.len_3[c]

        if self.ok1 == 0 and self.ok2 == 0 and self.ok3 == 0 and self.c1 == 0 and self.my <= 56 and 48 <= self.my and self.mx <= 48 and 40 <= self.mx and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.ok1 = 1
            self.ok2 = 1
            self.ok3 = 1
            self.c1 = 1
            self.c2 = 1
            self.c3 = 1
            self.p = 1
            self.coin -= 5

        if self.ok1 == 0 and self.ok2 == 0 and self.ok3 == 0 and self.c1 == 0 and self.p == 1:
            self.p = 0
            if self.stop[0][0] == self.stop[1][0] and self.stop[0][0] == self.stop[2][0]:
                if self.stop[0][0] == 0:
                    self.coin += 100
                if self.stop[0][0] == 1:
                    self.coin += 20
                if self.stop[0][0] == 2:
                    self.coin += 30
                if self.stop[0][0] == 3:
                    self.coin += 5
                if self.stop[0][0] == 4:
                    self.coin += 50
            if self.stop[0][1] == self.stop[1][1] and self.stop[0][1] == self.stop[2][1]:
                if self.stop[0][1] == 0:
                    self.coin += 100
                if self.stop[0][1] == 1:
                    self.coin += 20
                if self.stop[0][1] == 2:
                    self.coin += 30
                if self.stop[0][1] == 3:
                    self.coin += 5
                if self.stop[0][1] == 4:
                    self.coin += 50
            if self.stop[0][2] == self.stop[1][2] and self.stop[0][2] == self.stop[2][2]:
                if self.stop[0][2] == 0:
                    self.coin += 100
                if self.stop[0][2] == 1:
                    self.coin += 20
                if self.stop[0][2] == 2:
                    self.coin += 30
                if self.stop[0][2] == 3:
                    self.coin += 5
                if self.stop[0][2] == 4:
                    self.coin += 50
            if self.stop[0][0] == self.stop[1][1] and self.stop[0][0] == self.stop[2][2]:
                if self.stop[0][0] == 0:
                    self.coin += 100
                if self.stop[0][0] == 1:
                    self.coin += 20
                if self.stop[0][0] == 2:
                    self.coin += 30
                if self.stop[0][0] == 3:
                    self.coin += 5
                if self.stop[0][0] == 4:
                    self.coin += 50
            if self.stop[0][2] == self.stop[1][1] and self.stop[0][2] == self.stop[2][0]:
                if self.stop[0][2] == 0:
                    self.coin += 100
                if self.stop[0][2] == 1:
                    self.coin += 20
                if self.stop[0][2] == 2:
                    self.coin += 30
                if self.stop[0][2] == 3:
                    self.coin += 5
                if self.stop[0][2] == 4:
                    self.coin += 50

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(13)

        pyxel.blt(0 + self.x, self.len_y1[0] + self.y, 0, self.len_1[0] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[1] + self.y, 0, self.len_1[1] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[2] + self.y, 0, self.len_1[2] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[3] + self.y, 0, self.len_1[3] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[4] + self.y, 0, self.len_1[4] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[5] + self.y, 0, self.len_1[5] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[6] + self.y, 0, self.len_1[6] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[7] + self.y, 0, self.len_1[7] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[8] + self.y, 0, self.len_1[8] * 8, 0, 8, 8, 0)
        pyxel.blt(0 + self.x, self.len_y1[9] + self.y, 0, self.len_1[9] * 8, 0, 8, 8, 0)

        pyxel.blt(9 + self.x, self.len_y2[0] + self.y, 0, self.len_2[0] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[1] + self.y, 0, self.len_2[1] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[2] + self.y, 0, self.len_2[2] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[3] + self.y, 0, self.len_2[3] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[4] + self.y, 0, self.len_2[4] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[5] + self.y, 0, self.len_2[5] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[6] + self.y, 0, self.len_2[6] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[7] + self.y, 0, self.len_2[7] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[8] + self.y, 0, self.len_2[8] * 8, 0, 8, 8, 0)
        pyxel.blt(9 + self.x, self.len_y2[9] + self.y, 0, self.len_2[9] * 8, 0, 8, 8, 0)

        pyxel.blt(18 + self.x, self.len_y3[0] + self.y, 0, self.len_3[0] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[1] + self.y, 0, self.len_3[1] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[2] + self.y, 0, self.len_3[2] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[3] + self.y, 0, self.len_3[3] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[4] + self.y, 0, self.len_3[4] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[5] + self.y, 0, self.len_3[5] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[6] + self.y, 0, self.len_3[6] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[7] + self.y, 0, self.len_3[7] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[8] + self.y, 0, self.len_3[8] * 8, 0, 8, 8, 0)
        pyxel.blt(18 + self.x, self.len_y3[9] + self.y, 0, self.len_3[9] * 8, 0, 8, 8, 0)

        pyxel.bltm(0, 0, 0, 0, 0, 58, 80, 0)
        pyxel.text(8, 66, "coin:" + str(self.coin), 0)

App()
