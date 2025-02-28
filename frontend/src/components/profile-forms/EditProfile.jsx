import React from 'react'

function EditProfile() {
    const profile = useSelector(state => state.profile.profile);

    const [formData, setFormData] = useState({
      company: "",
      website: "",
      location: "",
      status: "",
      skills: "",
      githubusername: "",
      bio: "",
      twitter: "",
      facebook: "",
      linkedin: "",
      youtube: "",
      instagram: ""
    });
    const [displaySocialInputs, toggleSocialInputs] = useState(false);
    const dispatch = useDispatch();
  
    useEffect(() => {
      getCurrentProfile();
      setFormData({ ...profile });
    }, [profile]);
  
    const {
      company,
      website,
      location,
      status,
      skills,
      githubusername,
      bio,
      twitter,
      facebook,
      linkedin,
      youtube,
      instagram
    } = formData;
  
    const onChange = e => {
      setFormData({ ...formData, [e.target.name]: e.target.value });
    };
  
    const onSubmit = e => {
      e.preventDefault();
      dispatch(createProfile(formData, history, true));
    };
  return (
    <div>
      
    </div>
  )
}

export default EditProfile
