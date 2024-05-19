/* eslint-disable */
import ClassRoom from "./0-classroom.js";

export default function initializeRooms() {
  const sizes = [19, 20, 34];
  const classArr = [];

  for (const size of sizes) {
    classArr.push(new ClassRoom(size));
  }
  return classArr;
}
