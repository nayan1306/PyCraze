function writeToTerminal(text, type) {
    const terminalOutput = document.getElementById('output');
    if (type === 'command') {
      terminalOutput.innerHTML += `<p class="command">${text}</p>`;
    } else {
      terminalOutput.innerHTML += `<p><span class="typing-animation">${text}</span></p>`;
    }
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
  }

  setTimeout(() => {
    writeToTerminal("<span>{{quote}}</span>", 'command');
  }, 0);

  setTimeout(() => {
    writeToTerminal("<span>Terminal: Welcome, theprobablyharsh! List your skills.</span>", 'conversation');
  }, 1000);

  setTimeout(() => {
    writeToTerminal("<span>theprobablyharsh@terminal:~$ echo 'Data Science, ML, MLOps, SDLC, SQL, React, UX, Interaction Design, Figma'</span>", 'command');
  }, 2500);

  setTimeout(() => {
    writeToTerminal("<span>Terminal: Impressive skill set! What about your personality traits?</span>", 'conversation');
  }, 3500);

  setTimeout(() => {
    writeToTerminal("<span>theprobablyharsh@terminal:~$ echo 'INTP-A, analytical, curious'</span>", 'command');
  }, 5500);

  setTimeout(() => {
    writeToTerminal("<span>Terminal: Analytical mind, got it. What languages do you speak?</span>", 'conversation');
  }, 6500);

  setTimeout(() => {
    writeToTerminal("<span>theprobablyharsh@terminal:~$ echo 'English, Hindi (fluent), Gujarati (native), Telugu, French, Spanish (familiar), Sanskrit, Korean, Italian (learning)'</span>", 'command');
  }, 8500);

  setTimeout(() => {
    writeToTerminal("<span>Terminal: Multilingual, nice. Your mission?</span>", 'conversation');
  }, 9500);

  setTimeout(() => {
    writeToTerminal("<span>theprobablyharsh@terminal:~$ echo 'Navigate data, tech, and design with passion for innovation and learning.'</span>", 'command');
  }, 11500);

  setTimeout(() => {
    writeToTerminal("<span>Terminal: Keep exploring and innovating, theprobablyharsh!</span>", 'conversation');
  }, 13000);