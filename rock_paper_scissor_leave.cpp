//I wrote this code so long ago while learning c++ and I decided to share it and improved it a bit.
// I do not remember how I wrote it but I think I used a lot of functions and structures to make it more organized and easier to read.
// I might  improve it more in the future by adding more features and making it more interactive but for now I think it's good enough.
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <string>
using namespace std;
struct player {
	int matchs;
	int win;
	int loss;
	int tie;
	 player() {
		matchs = 0;
		win = 0;
		loss = 0;
		tie = 0;
	}
};
void preStartGame(player &player1 , player &bot1);
void startGame(string, string, player &, player &);
void showStats(player &, player &);
string bot_choice();
string get_valid_string(string message);
int get_valid_integer(string message);  //this is used to prevent the programme to crash when the user enter a letter.
int main() {
	srand(time(0));
	player player1, bot1, bot2; //this to save stats
	cout << "this is the rock paper scissor game." << endl;
	preStartGame(player1 , bot1);
}
string get_valid_string(string message) {  //this is used to get a valid string.
	string choice;
	int length;
	bool check_input = true;
	while (check_input == true) {
		cout << message;
		getline(cin, choice);
		length = choice.length();
		for (int c(0); c < length; c++) {
			choice[c] = tolower(choice[c]);
		}
		if ((choice == "rock") || (choice == "paper") || (choice == "scissor") || (choice == "leave")) {
			check_input = false;
		}
	}
	return choice;
}
string bot_choice() {
	string botChoice;
	int random_num(1 + rand() % 3);
	if (random_num == 1)
		botChoice = "rock";
	else if (random_num == 2)
		botChoice = "paper";
	else
		botChoice = "scissor";
	return 	botChoice;
}
void startGame(string humanChoice, string botChoice, player &player1, player &bot1) {
	if (humanChoice == botChoice) {
		cout << "\ntie!";
		player1.matchs+=1;
		bot1.matchs+=1;
		player1.tie+=1;
		bot1.tie+=1;
	}
	else if (((humanChoice == "rock") && (botChoice == "scissor")) || ((humanChoice == "paper") && (botChoice == "rock")) || ((humanChoice == "scissor") && (botChoice == "paper"))) {
		cout << "\nyou win!!";
		player1.matchs++;
		bot1.matchs++;
		player1.win++;
		bot1.loss++;

	}
	else {
		cout << "you lose!";
		player1.matchs++;
		bot1.matchs++;
		player1.loss++;
		bot1.win++;
	}

}
int get_valid_integer(string message){  //this is used to prevent the programme to crash when the user enter a letter.
	int number;
	bool check_input = true;
	while (check_input == true){
	cout<< message ;
	cin >> number ;
	if (cin.fail()){
	cin.clear();
	cin.ignore(1000, '\n');
	cout<< "please enter the input correctly!.\n";
		}
	else
	check_input = false;
}
	return number;	
}
void showStats(player &player1 , player &bot1) {
	int choice;
	cout << "--------------------------------------------------------------------------------" << endl;
	cout << "you played: " << player1.matchs << endl;
	cout << "you won: " << player1.win << endl;
	cout << "you lost: " << player1.loss << endl;
	cout<< "you tied: "<< player1.tie << endl;
	cout << "--------------------------------------------------------------------------------" << endl;
	choice = get_valid_integer("do you want to play again?\npress 1 if yes: ");
	if (choice == 1){
		cin.ignore(1000, '\n');
		preStartGame(player1 , bot1);
	}
	else
	cout<< "ok";
	
}
void preStartGame(player &player1 , player &bot1){
	string botChoice, humanChoice("hello world"); //to save both choices
	while (humanChoice != "leave") {
	humanChoice = get_valid_string("\nEnter one of the four choices(rock , scissor , paper , leave): \n");
	botChoice = bot_choice();
	if (humanChoice != "leave")
		startGame(humanChoice, botChoice, player1, bot1);
	else {
		showStats(player1 , bot1);
		}
	}
}