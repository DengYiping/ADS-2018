#include <algorithm>
#include <queue>
#include <vector>

#define MAX(A,B) (((A)>(B))?(A):(B))

using namespace std;

struct Node {
    int index;
    int dx;
    int dy;
};

int main(int argc, char** argv){
    return 0;
}

int find_meetup_city(int** adj_matrix, int your_city, int friend_city,int n)
{

    /*
     * Comparision function for priority queue
     * comparre with respect to x and y
     */
    auto cmp_x = [](Node* left, Node* right) { return (left->dx) > (right->dx);};
    auto cmp_y = [](Node* left, Node* right) { return (left->dy) > (right->dy);};

    vector<Node*> vec;

    for(int i = 0; i < n; i++){
        Node* node = new Node();

        node->dx = 0x7fffffff; //max value for int
        node->dy = 0x7fffffff; //max value for int
        node->index = i;

        vec.push_back(node);
    }

    //priority queue
    priority_queue<Node*, std::vector<Node*>, decltype(cmp_x)> qx(cmp_x);
    priority_queue<Node*, std::vector<Node*>, decltype(cmp_y)> qy(cmp_y);

    /*
     * Dijkstra on dx value of the node
     */

    vec[your_city]->dx = 0; //set the value to city itself to be 0
    qx.push(vec[your_city]); //put into the queue

    while(qx.empty() == false){
        //main loop
        Node* v = qx.top();
        qx.pop(); //remove the top

        for(int i = 0; i < n; i++){
            if(i != v->index){
                Node* v1 = vec[i];
                if(v1->dx > (v->dx + adj_matrix[v->index][i])){
                    v1->dx = v->dx + adj_matrix[v->index][i];
                    qx.push(v1);
                }
            }
        }
    }
    /*
     * Dijkstra on dy value of the node
     */

    vec[friend_city]->dy = 0;
    qy.push(vec[friend_city]);

    while(qy.empty() == false){
        Node* v = qy.top();
        qy.pop();

        for(int i = 0; i < n; i++){
            if(i != v->index){
                Node* v1 = vec[i];
                if(v1->dy > (v->dy + adj_matrix[v->index][i])){
                    v1->dy = v->dy + adj_matrix[v->index][i];
                    qx.push(v1);
                }
            }
        }
    }



    //sort the vector accordingly
    sort(vec.begin(), vec.end(), [](Node* a, Node* b){
            return MAX(a->dx, a->dy) < MAX(b->dx, b->dy);
            });

    int rst = vec[0]->index;
    for(int i = 0; i < n; i++){
        delete vec[i];
    }
    return rst;
}


