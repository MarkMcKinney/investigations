/* 
BITWISE FLAGS
-----------------------------------------------
I wanted to explore bit manipulation. After 
some brief reading, I took a look at bitwise 
operations and more efficient ways for setting 
and storing flags.
*/

// Default is all flags are off
let setFlags = 00000000;

// Flag Options
const cyanFlag = 00000001;
const blueFlag = 00000010;
const limeFlag = 00000100;


// Remove a flag from user's set flags
const flagRemove = ({queryFlag}) => {
    setFlags ^= queryFlag;
    return setFlags;
}

// Set the cyan and blue flag
setFlags |= cyanFlag;
setFlags |= blueFlag;

// Check if lime and cyan flag is set
console.log("Lime is set: ", setFlags & limeFlag ? true : false)
console.log("Cyan is set: ", setFlags & cyanFlag ? true : false)
// Remove the cyan flag
setFlags ^= cyanFlag
// Re-check if the cyan flag is set
console.log("Cyan is set: ", setFlags & cyanFlag ? true : false)