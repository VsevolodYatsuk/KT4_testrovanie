import requests
import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.Graph()
G.add_node("Dog API")
G.add_node("Get random dog image")
G.add_node("List all breeds")
G.add_node("Get breed image")

G.add_edge("Dog API", "Get random dog image")
G.add_edge("Dog API", "List all breeds")
G.add_edge("Dog API", "Get breed image")


pos = nx.spring_layout(G, seed=42)
labels = {node: node for node in G.nodes()}

nx.draw(G, pos, with_labels=True, labels=labels, node_size=5000, node_color='skyblue', font_size=10)
plt.title("Dog API MindMap")
plt.axis('off')


plt.savefig("dog_api_mindmap.png", format="PNG")
plt.show()

def test_api_endpoint(url):
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert 'message' in data

def create_test_report():
    with open("dog_api_test_report.txt", "w") as report:
        report.write("Dog API Test Report\n\n")

        report.write("1. Test: Get random dog image\n")
        test_api_endpoint("https://dog.ceo/api/breeds/image/random")
        report.write("   Passed\n\n")

        report.write("2. Test: List all breeds\n")
        test_api_endpoint("https://dog.ceo/api/breeds/list/all")
        report.write("   Passed\n\n")

        report.write("3. Test: Get breed image\n")
        test_api_endpoint("https://dog.ceo/api/breed/labrador/images/random")  # Replace with a valid breed name
        report.write("   Passed\n\n")

        report.write("4. Test: Invalid breed name\n")
        response = requests.get("https://dog.ceo/api/breed/invalid_breed/images/random")
        assert response.status_code == 404
        report.write("   Passed\n\n")

        report.write("5. Test: Sub-breeds\n")
        test_api_endpoint("https://dog.ceo/api/breed/collie/list")  # Replace with a valid breed name with sub-breeds
        report.write("   Passed\n")

create_test_report()
