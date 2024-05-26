/* eslint-disable */
import {uploadPhoto, createUser} from './utils';

export default function handleProfileSignup() {
  const photo = uploadPhoto();
  const user = createUser();
  return Promise.all([photo, user]).then((body) => {
    const [photo, user] = body;
    console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
  }).catch(() => console.log('Signup system offline'))};
