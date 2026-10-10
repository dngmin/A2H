#include <iostream>
#include <string>
#include <unordered_map>
// copy
#include <cstdio>

std::unordered_map<std::string, int> L_map = {
    {"r",  0},   // ㄱ
    {"R",  1},   // ㄲ
    {"s",  2},   // ㄴ
    {"e",  3},   // ㄷ
    {"E",  4},   // ㄸ
    {"f",  5},   // ㄹ
    {"a",  6},   // ㅁ
    {"q",  7},   // ㅂ
    {"Q",  8},   // ㅃ
    {"t",  9},   // ㅅ
    {"T", 10},   // ㅆ
    {"d", 11},   // ㅇ
    {"w", 12},   // ㅈ
    {"W", 13},   // ㅉ
    {"c", 14},   // ㅊ
    {"z", 15},   // ㅋ
    {"x", 16},   // ㅌ
    {"v", 17},   // ㅍ
    {"g", 18}    // ㅎ
};

std::unordered_map<std::string, int> V_map = {
    {"k",  0},   // ㅏ
    {"o",  1},   // ㅐ
    {"i",  2},   // ㅑ
    {"O",  3},   // ㅒ
    {"j",  4},   // ㅓ
    {"p",  5},   // ㅔ
    {"u",  6},   // ㅕ
    {"P",  7},   // ㅖ
    {"h",  8},   // ㅗ
    {"hk", 9},   // ㅘ
    {"ho", 10},  // ㅙ
    {"hl", 11},  // ㅚ
    {"y", 12},   // ㅛ
    {"n", 13},   // ㅜ
    {"nj", 14},  // ㅝ
    {"np", 15},  // ㅞ
    {"nl", 16},  // ㅟ
    {"b", 17},   // ㅠ
    {"m", 18},   // ㅡ
    {"ml", 19},  // ㅢ
    {"l", 20}    // ㅣ
};

std::unordered_map<std::string, int> T_map = {
    {"",   0},   // 終声なし
    {"r",  1},   // ㄱ
    {"R",  2},   // ㄲ
    {"rt", 3},   // ㄳ
    {"s",  4},   // ㄴ
    {"sw", 5},   // ㄵ
    {"sg", 6},   // ㄶ
    {"e",  7},   // ㄷ
    {"f",  8},   // ㄹ
    {"fr", 9},   // ㄺ
    {"fa", 10},  // ㄻ
    {"fq", 11},  // ㄼ
    {"ft", 12},  // ㄽ
    {"fx", 13},  // ㄾ
    {"fv", 14},  // ㄿ
    {"fg", 15},  // ㅀ
    {"a", 16},   // ㅁ
    {"q", 17},   // ㅂ
    {"qt", 18},  // ㅄ
    {"t", 19},   // ㅅ
    {"T", 20},   // ㅆ
    {"d", 21},   // ㅇ
    {"w", 22},   // ㅈ
    {"c", 23},   // ㅊ
    {"z", 24},   // ㅋ
    {"x", 25},   // ㅌ
    {"v", 26},   // ㅍ
    {"g", 27}    // ㅎ
};

std::string Hangul2Utf8(char32_t HangulIndex)
{
    char32_t code = 0xAC00 + HangulIndex;
    std::string result;

    result += static_cast<char>(0xE0 | (code >> 12));
    result += static_cast<char>(0x80 | ((code >> 6) & 0x3F));
    result += static_cast<char>(0x80 | (code & 0x3F));

    return result;
}

// unicode 3byte 変換
// if code = 0xAC00 + 433
// code -> 0xADB1(16) -> 1010110110110001(2) -> 1010 110110 110001
// unicode 3byte st.に変換(1110xxxx 10xxxxxx 10xxxxxx)(xに入る)
// 変換後 : 11101010 10110110 10110001(2) -> EAB6B1(16)

void copy(const std::string& text)
// Linuxは対応しない
{
    #if defined(__APPLE__)
        // macOS
        FILE* pipe = popen("pbcopy", "w");
    #elif defined(_WIN32)
        // Window
        FILE* pipe = _popen("clip", "w");
    #else
        return;
    #endif
    if (pipe) 
    {
        fwrite(text.data(), 1, text.size(), pipe);

        #if defined(__APPLE__)
            pclose(pipe);
        #elif defined(_WIN32)
            _pclose(pipe);
        #endif
    }
}

void run()
{
    std::string Input; std::getline(std::cin, Input);
    std::string output = "";
    std::string V = "", T = "";


    for (int i = Input.size()-1; i >= 0; i--)
    {
        char element = Input[i];
        if (('a' <= element and element <= 'z') or ('A' <= element and element <= 'Z'))
        {
            if (V_map.find(std::string(1, element)) != V_map.end())
            {
                V = element + V;
            }
            else
            {
                if (V != "")
                {
                    // elementがLにないと新しく追加してしまうことを修正
                    int L_index = L_map[std::string(1, element)], V_index = V_map[V], T_index = T_map[T];
                    int HangulIndex = (L_index * 21 + V_index) * 28 + T_index;
                    output = Hangul2Utf8(HangulIndex) + output;
                    V = "";
                    T = "";
                }
                else
                {
                    T = element + T;
                }
            }
        }
        else output = std::string(1, element) + output;
    }

    // std::cout << output;
    copy(output);

    return;
}

int main()
{
    while (1) run();
}


// g++ -std=c++20 prototype/core/cpp.cpp -o proto