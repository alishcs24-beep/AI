{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNzHIHsSdP1wrzY1lfZkFjO",
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
        "<a href=\"https://colab.research.google.com/github/alishcs24-beep/AI/blob/main/1WA24CS035_Week7_FOL_Unification.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g6JGCn1MgOk4",
        "outputId": "2202a823-c144-4ba9-e062-8496bb014937"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "FIRST ORDER LOGIC - UNIFICATION\n",
            "Unification Successful!\n",
            "Most General Unifier (MGU): {'x': 'b'}\n"
          ]
        }
      ],
      "source": [
        "\n",
        "\n",
        "def is_variable(x):\n",
        "    return isinstance(x, str) and x.islower() and x.isalpha()\n",
        "\n",
        "\n",
        "def occurs_check(var, term, subst):\n",
        "    term = substitute(term, subst)\n",
        "\n",
        "    if var == term:\n",
        "        return True\n",
        "\n",
        "    if isinstance(term, tuple):\n",
        "        return any(occurs_check(var, arg, subst) for arg in term)\n",
        "\n",
        "    return False\n",
        "\n",
        "\n",
        "def substitute(term, subst):\n",
        "    if isinstance(term, str):\n",
        "        while term in subst:\n",
        "            term = subst[term]\n",
        "        return term\n",
        "\n",
        "    if isinstance(term, tuple):\n",
        "        return tuple(substitute(arg, subst) for arg in term)\n",
        "\n",
        "    return term\n",
        "\n",
        "\n",
        "def unify(x, y, subst=None):\n",
        "    if subst is None:\n",
        "        subst = {}\n",
        "\n",
        "    x = substitute(x, subst)\n",
        "    y = substitute(y, subst)\n",
        "\n",
        "    if x == y:\n",
        "        return subst\n",
        "\n",
        "    if is_variable(x):\n",
        "        if occurs_check(x, y, subst):\n",
        "            return None\n",
        "        subst[x] = y\n",
        "        return subst\n",
        "\n",
        "    if is_variable(y):\n",
        "        if occurs_check(y, x, subst):\n",
        "            return None\n",
        "        subst[y] = x\n",
        "        return subst\n",
        "\n",
        "    if isinstance(x, tuple) and isinstance(y, tuple):\n",
        "        if len(x) != len(y) or x[0] != y[0]:\n",
        "            return None\n",
        "\n",
        "        for a, b in zip(x[1:], y[1:]):\n",
        "            subst = unify(a, b, subst)\n",
        "            if subst is None:\n",
        "                return None\n",
        "\n",
        "        return subst\n",
        "\n",
        "    return None\n",
        "\n",
        "\n",
        "# Main program\n",
        "print(\"FIRST ORDER LOGIC - UNIFICATION\")\n",
        "\n",
        "expr1 = (\"P\", \"x\", \"a\")\n",
        "expr2 = (\"P\", \"b\", \"a\")\n",
        "\n",
        "result = unify(expr1, expr2)\n",
        "\n",
        "if result is not None:\n",
        "    print(\"Unification Successful!\")\n",
        "    print(\"Most General Unifier (MGU):\", result)\n",
        "else:\n",
        "    print(\"Unification Failed!\")\n"
      ]
    }
  ]
}