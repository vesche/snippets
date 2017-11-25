using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerStats : MonoBehaviour {

	public int currentLevel;

	public int currentExp;

	public int[] toLevelUp;

	public int[] HPLevels;
	public int[] attackLevels;
	public int[] defenceLevels;

	public int currentHP;
	public int currentAttack;
	public int currentDefence;

	private PlayerHealthManager thePlayerHealth;

	// Use this for initialization
	void Start () {
		currentHP = HPLevels [1];
		currentAttack = attackLevels [1];
		currentDefence = defenceLevels [1];

		thePlayerHealth = FindObjectOfType<PlayerHealthManager> ();
	}
	
	// Update is called once per frame
	void Update () {
		if (currentExp >= toLevelUp [currentLevel]) 
		{
			//currentLevel++;
			levelUp();
		}
			
	}

	public void AddExperience(int experienceToAdd)
	{
		currentExp += experienceToAdd;
	}

	public void levelUp()
	{
		currentLevel++;
		currentHP = HPLevels [currentLevel];

		thePlayerHealth.playerMaxHealth = currentHP;
		thePlayerHealth.playerCurrentHealth = currentHP;
		//thePlayerHealth.playerCurrentHealth += currentHP - HPLevels [currentLevel - 1];

		currentAttack = attackLevels [currentLevel];
		currentDefence = defenceLevels [currentLevel];
	}
}

