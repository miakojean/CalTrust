def post(self, request, *args, **kwargs):
    serializer = UserRegistrationSerializer(data=request.data)
    
    if serializer.is_valid():
        user_profile = serializer.save() 
        
        response_data = {
            "message": "User and profile created successfully!",
            "username": user_profile.user.username,
            "email": user_profile.user.email,
            "user_type": "customer" if isinstance(user_profile, CustomerProfile) else "firm"
        }
        
        # Modifier cette partie pour utiliser les champs directs de FirmProfile
        if isinstance(user_profile, FirmProfile):
            response_data["company_details"] = {
                "name": user_profile.company_name,  # Champ direct
                "siret": user_profile.siret,        # Champ direct
                "address": user_profile.address     # Champ direct
                # Supprimer 'category' car il n'existe pas dans le modèle actuel
            }
        
        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)