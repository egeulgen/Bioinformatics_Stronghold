#include <iostream>
#include <fstream>
using namespace std;

bool inside_band(int i, int j, int k) {
	return i - j >= -k && i - j <= k;
}

int** edit_distance_kband(string seq1, string seq2, int bandwidth)
{
	int m = seq1.length() + 1; 
	int n = seq2.length() + 1;
	
	int diff = m - n;

	int** score_mat = new int*[m];
	
	for (int i = 0; i < m; i ++)
	{
		score_mat[i] = new int[n];
		for (int j = 0; j < n; j ++)
		{
			score_mat[i][j] = 1e6;
		}
	}

	for (int i = 0; i <= bandwidth + diff; i++)
	{
		score_mat[i][0] = i;
	}

	for (int j = 1; j <= bandwidth; j++)
	{
		score_mat[0][j] = j;
	}
	
	for (int i = 1; i < m; i++)
	{
		for (int h = - bandwidth - diff; h <= bandwidth; h++) {
			int j = i + h;

			if (j >= 1 && j < n)
			{
				// cout << i << " " << j << "\n";

				score_mat[i][j] = score_mat[i - 1][j -1];
				if (seq1[i - 1] != seq2[j - 1])
				{
					score_mat[i][j] = score_mat[i - 1][j -1] + 1;
				}

				if (inside_band(i - 1, j, bandwidth + diff))
				{
					int tmp = score_mat[i - 1][j] + 1;
					if (score_mat[i][j] > tmp)
					{
						score_mat[i][j] = score_mat[i - 1][j] + 1;
					}
				}
				if (inside_band(i, j - 1, bandwidth))
				{
					int tmp = score_mat[i][j - 1] + 1;
					if (score_mat[i][j] > tmp)
					{
						score_mat[i][j] = tmp;
					}
				}
			}

		}
	}

	return score_mat;
}

int main()
{
	fstream in_file;
	
	in_file.open("/Users/egeulgen/Downloads/rosalind_ksim.txt",ios::in);

	string motif;
	string sequence;
	int k;

	if (in_file.is_open())
	{
		string tmp;
		int count = 0;
		while (count < 3)
		{
			std::getline(in_file, tmp);
			if (count == 0) {
				k = std::stoi(tmp);
			} else if (count == 1) {
				motif = tmp;
			} else {
				sequence = tmp;
			}
			count += 1;
		}
		in_file.close(); //close the file object.
	}

	// cout << k << "\n";
	// cout << motif << "\n";
	// cout << sequence << "\n";

	int len_motif = motif.length();
	int len_sequence = sequence.length();

	int last = 0;
	string substr = "";
	int len_substr = 0;

	int max_s = len_sequence - len_motif + k;

	#pragma omp parallel for
	for (int i = 0; i <= max_s; i ++)
	{
		// cout << i << "/////////\n";

		if (len_sequence < i + len_motif + k + 1)
		{
			last = len_sequence;
		} else
		{
			last = i + len_motif + k + 1;
		}

		substr = sequence.substr(i, last - i);
		len_substr = substr.length();

		if (len_substr < len_motif)
		{
			int** score_mat = edit_distance_kband(motif, substr, k);
			
			int idx = len_substr;
			while (score_mat[len_motif][idx] != 1e6)
			{
				if (score_mat[len_motif][idx] <= k)
				{
					cout << i + 1 << " " << idx << "\n";
				}
				idx -= 1;
			}

			for (int i = 0; i <= len_motif; i ++)
			{
				delete [] score_mat[i];
			}
			delete [] score_mat;
		} else
		{
			int** score_mat = edit_distance_kband(substr, motif, k);
			
			int idx = len_substr;
			while (score_mat[idx][len_motif] != 1e6)
			{
				if (score_mat[idx][len_motif] <= k)
				{
					cout << i + 1 << " " << idx << "\n";
				}
				idx -= 1;
			}
			for (int i = 0; i <= len_substr; i ++)
			{
				delete [] score_mat[i];
			}
			delete [] score_mat;
		}
	}
	return 0;
}