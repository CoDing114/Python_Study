class ThailandPackage:
    def detail(self):
        print("태국 패키지")

if __name__ == "__main__":
    print("ThailandPackage 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("ThailandPackage 외부에서 모듈 호출")