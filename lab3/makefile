CXX = g++
CXXFLAGS = -Wall
SRC = main.cpp candidate.cpp voting.cpp
TARGET = voting

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

clean:
	del $(TARGET).exe 2>nul || rm -f $(TARGET)