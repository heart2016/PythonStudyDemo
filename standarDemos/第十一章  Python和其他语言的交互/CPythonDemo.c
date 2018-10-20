#include<string.h>

//判断一个字符串是不是对称的字符串
int is_symmetry(char * text){
	int i,n = strlen(text);
	
	for(int i=0; i<n/2;i++){
		if(text[i] != text[n-i-1]) return 0;
	}
	return 1;
}