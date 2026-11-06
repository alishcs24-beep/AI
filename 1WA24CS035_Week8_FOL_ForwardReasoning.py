{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMDYw/tdzLdGLyRHB8eRjN5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/alishcs24-beep/AI/blob/main/1WA24CS035_Week8_FOL_ForwardReasoning.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e7cnV5jaktLx",
        "outputId": "4741ce43-afbc-4696-e450-f447b88826d1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Initial Knowledge Base:\n",
            "('Parent', 'Ravi', 'Amit')\n",
            "('Parent', 'Amit', 'Rahul')\n",
            "\n",
            "Applying Forward Chaining...\n",
            "\n",
            "Derived: ('Grandparent', 'Ravi', 'Rahul')\n",
            "\n",
            "Query Proved Successfully!\n",
            "Query: ('Grandparent', 'Ravi', 'Rahul')\n"
          ]
        }
      ],
      "source": [
        "\n",
        "facts = [\n",
        "    (\"Parent\", \"Ravi\", \"Amit\"),\n",
        "    (\"Parent\", \"Amit\", \"Rahul\")\n",
        "]\n",
        "\n",
        "\n",
        "query = (\"Grandparent\", \"Ravi\", \"Rahul\")\n",
        "\n",
        "\n",
        "def forward_chaining(facts, query):\n",
        "    inferred = True\n",
        "\n",
        "    while inferred:\n",
        "        inferred = False\n",
        "\n",
        "\n",
        "        parents = [f for f in facts if f[0] == \"Parent\"]\n",
        "\n",
        "        for p1 in parents:\n",
        "            for p2 in parents:\n",
        "\n",
        "                if p1[2] == p2[1]:\n",
        "                    new_fact = (\n",
        "                        \"Grandparent\",\n",
        "                        p1[1],\n",
        "                        p2[2]\n",
        "                    )\n",
        "\n",
        "                    if new_fact not in facts:\n",
        "                        facts.append(new_fact)\n",
        "                        inferred = True\n",
        "\n",
        "                        print(\"Derived:\", new_fact)\n",
        "\n",
        "    return query in facts\n",
        "\n",
        "\n",
        "print(\"Initial Knowledge Base:\")\n",
        "for fact in facts:\n",
        "    print(fact)\n",
        "\n",
        "print(\"\\nApplying Forward Chaining...\\n\")\n",
        "\n",
        "if forward_chaining(facts, query):\n",
        "    print(\"\\nQuery Proved Successfully!\")\n",
        "    print(\"Query:\", query)\n",
        "else:\n",
        "    print(\"\\nQuery Cannot Be Proved.\")\n"
      ]
    }
  ]
}