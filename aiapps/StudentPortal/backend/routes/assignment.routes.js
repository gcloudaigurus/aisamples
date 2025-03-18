const express = require('express');
const { auth, isAdmin } = require('../middleware/auth.middleware');
const { Assignment } = require('../models');
const router = express.Router();

// Create assignment (admin only)
router.post('/', auth, isAdmin, async (req, res) => {
  try {
    const assignment = await Assignment.create(req.body);
    res.status(201).send(assignment);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Get assignment by ID
router.get('/:id', auth, async (req, res) => {
  try {
    const assignment = await Assignment.findByPk(req.params.id);
    if (!assignment) {
      return res.status(404).send({ error: 'Assignment not found' });
    }
    res.send(assignment);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Update assignment (admin only)
router.put('/:id', auth, isAdmin, async (req, res) => {
  try {
    const assignment = await Assignment.findByPk(req.params.id);
    if (!assignment) {
      return res.status(404).send({ error: 'Assignment not found' });
    }

    const updates = Object.keys(req.body);
    updates.forEach(update => assignment[update] = req.body[update]);
    await assignment.save();
    
    res.send(assignment);
  } catch (error) {
    res.status(400).send(error);
  }
});

// Delete assignment (admin only)
router.delete('/:id', auth, isAdmin, async (req, res) => {
  try {
    const assignment = await Assignment.findByPk(req.params.id);
    if (!assignment) {
      return res.status(404).send({ error: 'Assignment not found' });
    }

    await assignment.destroy();
    res.send({ message: 'Assignment deleted successfully' });
  } catch (error) {
    res.status(500).send(error);
  }
});

module.exports = router; 