lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java", "C++"]
# lenguajes.insert(3, "Ada")  # Insertar "Ada" entre "PHP" y "JavaScript".
lenguajes.insert(3, "Ruby")  # Insertar "Ada" entre "PHP" y "JavaScript".
print(lenguajes)
lenguajes.remove("Ruby")    # Elimina el primer "Ruby" que encuentre.
print(lenguajes)
print("La lista tiene", len(lenguajes), "elementos.")
print(f"La lista tiene {len(lenguajes)} elementos.")