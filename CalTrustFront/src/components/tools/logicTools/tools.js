function getInitials(name) {
    if (typeof name !== 'string') return '';

    const words = name.trim().split(/\s+/); // Sépare les mots par les espaces
    const firstTwoWords = words.slice(0, 2); // Garde les deux premiers mots

    const initials = firstTwoWords
        .map(word => word.charAt(0).toUpperCase()) // Prend la première lettre
        .join('');

    return initials;
}

export { getInitials };