file = open("index.h", "w")
file.write("#include <iostream>" + '\n')
file.write("void helloA() {" + '\n')
file.write("    std::cout << \"hello from A\" << std::endl;" + '\n')
file.write("}" + '\n')
file.close()
