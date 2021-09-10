class VietnamPackage:
    def detail(self):
        print("베트남 패키지")

if __name__ == "__main__":
    print("VietnamPackage 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = VietnamPackage()
    trip_to.detail()
else:
    print("VietnamPackage 외부에서 모듈 호출")